from sketch import disableFeatures, disableClean
from features import switchFeatures
from problems import *
from textbook_problems import *
from countingProblems import CountingProblem
from utilities import *
from parseSPE import parseSolution

from fragmentGrammar import FragmentGrammar
from matrix import *
from randomSampleSolver import RandomSampleSolver
from incremental import IncrementalSolver

import argparse
from multiprocessing import Pool
import sys
import io

from command_server import start_server

def exportPath():
    importantArguments = ["features", "disableClean", "window"]    
    p = arguments.problem + "_" + arguments.task + "_" + "_".join("%s=%s"%(k, arguments.__dict__[k])
                                                                  for k in sorted(importantArguments)
                                                                  if arguments.__dict__[k] is not None)
    if arguments.universal:
        p += "_ug"
    p += ".p"
    return "experimentOutputs/" + p

def handleProblem(p):
    random.seed(arguments.seed)

    if arguments.restrict != None:
        print "(Restricting problem data to interval: %d -- %d)"%(arguments.restrict[0],arguments.restrict[1])
        restriction = p.data[arguments.restrict[0] : arguments.restrict[1]]
    else: restriction = p.data
        
    print p.description
    isCountingProblem = isinstance(p.parameters, list) \
                        and all( isinstance(parameter,int) for parameter in p.parameters  )
    if not isCountingProblem:
        print formatTable([ map(unicode,inflections) for inflections in restriction ])
    else:
        print CountingProblem(p.data, p.parameters, problemName=p.key).latex()

    if arguments.universal != None:
        assert arguments.universal.endswith('.p')
        universalGrammarPath = arguments.universal
            
        if not os.path.exists(universalGrammarPath):
            print "Fatal error: Cannot find universal grammar",universalGrammarPath
            assert False
            
        ug = FragmentGrammar.load(universalGrammarPath)
        print "Loaded %s:\n%s"%(universalGrammarPath,ug)
    else: ug = None

    startTime = time()

    ss = None # solutions to save out to the pickled file
    accuracy, compression = None, None
    
    if isCountingProblem:
        problem = CountingProblem(p.data, p.parameters, problemName=p.key)
        arguments.task = 'exact'
    else:
        problem = UnderlyingProblem(p.data, problemName=p.key, UG = ug).restrict(restriction)
    
    if arguments.task == 'debug':
        for s in p.solutions:
            s = parseSolution(s)
            problem.debugSolution(s,Morph(tokenize(arguments.debug)))
        sys.exit(0)
    elif arguments.task == 'verify':
        for s in p.solutions:
            s = parseSolution(s)
            print "verifying:"
            print s
            b = UnderlyingProblem(p.data).bank
            for r in s.rules:
                print "Explaining rule: ",r
                r.explain(b)
            problem.illustrateSolution(s)
        sys.exit(0)
        
    elif arguments.task == 'ransac':
        assert False, "ransac solver is deprecated"
    elif arguments.task == 'incremental':
        ss = IncrementalSolver(p.data,arguments.window,UG = ug,
                               problemName = p.key,
                               numberOfCPUs = 1 if arguments.serial else None,
                               globalTimeout=arguments.timeout*60*60 if arguments.timeout is not None else None).\
             restrict(restriction)
        if arguments.alignment: ss.loadAlignment('precomputedAlignments/%s.p'%(p.key))
        result = ss.incrementallySolve(resume = arguments.resume,                                
                                   k = arguments.top)
    elif arguments.task == 'CEGIS':
        ss = problem
        if arguments.alignment: ss.loadAlignment('precomputedAlignments/%s.p'%(p.key))
        result = ss.counterexampleSolution(k = arguments.top)
    elif arguments.task == 'exact':
        if arguments.alignment: problem.loadAlignment('precomputedAlignments/%s.p'%(p.key))
        result = Result(p.key)
        s = problem.sketchJointSolution(1, canAddNewRules = True)
        result.recordSolution(s)
        ss = problem.expandFrontier(s, arguments.top)
        result.recordFinalFrontier(ss)
    elif arguments.task == 'frontier':
        seed = arguments.restore
        if not os.path.exists(seed):
            assert False, "Could not find path %s"%seed
        result = loadPickle(seed)
        assert isinstance(result, Result)
        worker = problem
        seed = worker.solveUnderlyingForms(result.finalFrontier.MAP()c)
        frontier = worker.solveFrontiers(seed, k = arguments.top)
        result.finalFrontier = frontier
        print frontier
        #dumpPickle(result, arguments.save or arguments.restore)
        sys.exit(0)

    print "Total time taken by problem %s: %f seconds"%(p.key, time() - startTime)

    result.parameters = arguments
    dumpPickle(result, exportPath())
    print "Exported experiment to",exportPath()        
                


def paretoFrontier(p):
    from time import time
    
    print p.description
    name = p.key
    random.seed(0)
    data = randomlyPermute(p.data)
    print "\n".join(map(str,data))
    if arguments.restrict:
        print "(Restricting problem data to interval: %d -- %d)"%(arguments.restrict[0],
                                                                  arguments.restrict[1])
        data = data[arguments.restrict[0] : arguments.restrict[1]]
        print "\n".join(map(str,data))
    p = UnderlyingProblem(data)
    paretoFront = p.paretoFront(3, 10, 1,
                                morphologicalCoefficient=1,
                                useMorphology=True)
    if arguments.pickleDirectory is not None:
        t = int(time())
        path = arguments.pickleDirectory + "/" + name + "_" + str(t) + "_paretoFrontier.p"
        dumpPickle(paretoFront, path)
        print "Exported Pareto frontier to",path
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solve jointly for morphology and phonology given surface inflected forms of lexemes')
    parser.add_argument('problem')
    parser.add_argument('task',
                        choices = ["CEGIS","incremental","ransac","exact",
                                   "debug","verify","frontier","pareto"],
                        default = "CEGIS",
                        type = str,
                        help = "The task you are asking the driver to initiate.")
    parser.add_argument('--features',
                        choices = ["none","sophisticated","simple"],
                        default = "sophisticated",
                        type = str,
                        help = "What features the solver allowed to use")
    parser.add_argument('-t','--top', default = 1, type = int)
    parser.add_argument('-m','--cores', default = None, type = int)
    parser.add_argument('--timeout', default = None, type = float,
                        help = 'global timeout. can be a real number. measured in hours.')
    parser.add_argument('--serial', default = False, action = 'store_true',
                        help = 'Run the incremental solver in serial mode (no parallelism)')
    parser.add_argument('--alignment', default = False, action = 'store_true')
    parser.add_argument('--disableClean', default = False, action = 'store_true',
                        help = 'disable kleene star')
    parser.add_argument('--resume', default = False, action = 'store_true',
                        help = 'Resume the incremental solver from the last checkpoint')
    parser.add_argument('--dummy', default = False, action = 'store_true',
                        help = 'Dont actually run the solver for ransac')
    parser.add_argument('-s','--seed', default = '0', type = str)
    parser.add_argument('-u','--universal', default = None, type = str)
    parser.add_argument('--window', default = None, type = int)
    parser.add_argument('--save', default = None, type = str)
    parser.add_argument('--restore', default = None, type = str)
    parser.add_argument('--debug', default = None, type = lambda s: unicode(s,'utf8'))
    parser.add_argument('--restrict', default = None, type = str)
    parser.add_argument('--samples', default = 30, type = int)
    parser.add_argument('-V','--verbosity', default = 0, type = int)

    arguments = parser.parse_args()
    setVerbosity(arguments.verbosity)

    if arguments.cores is None:
        arguments.cores = numberOfCPUs()
    
    if arguments.features == "none":
        disableFeatures()
    else:
        print "Using the `%s` feature set"%(arguments.features)
        switchFeatures(arguments.features)
        
    if arguments.disableClean:
        disableClean()
    
    try:
        problem = int(arguments.problem)
    except:
        try:
            problem = Problem.named[arguments.problem]
        except:
            print("Could not find problem %s"%problem)
            sys.exit(0)            

    if arguments.restrict != None:        
        restriction = tuple(map(int,[offset for offset in arguments.restrict.split(":") if offset != '']))
        if len(restriction) == 1:
            if arguments.restrict.startswith(":"):
                restriction = [0,restriction[0]]
            elif arguments.restrict.endswith(":"):
                restriction = [restriction[0],99999]
            else:
                assert False, ("Invalid restriction expression:"+arguments.restrict)
        arguments.restrict = restriction

    start_server(arguments.cores)

    if arguments.task == "pareto":
        # a quick hack
        paretoFrontier(problem)
        sys.exit(0)
        

    displayTimestamp("Executing driver")
    handleProblem(problem)
        
