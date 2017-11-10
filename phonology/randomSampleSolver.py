# -*- coding: utf-8 -*-

from matrix import *
from incremental import IncrementalSolver

from pathos.multiprocessing import ProcessingPool as Pool
from time import time
import random
from sketch import setGlobalTimeout
import traceback

class RandomSampleSolver(IncrementalSolver):
    def __init__(self, data, timeout, lower, upper, UG = None, dummy = False):
        super(self.__class__,self).__init__(data, window = 2, UG = UG, numberOfCPUs = 1)

        self.dummy = dummy
        self.timeout = timeout
        self.lower = lower
        self.upper = min(upper, len(self.data))

    def worker(self, seed):
        try:
            random.seed(seed)
            startTime = time()

            solutions = []

            setGlobalTimeout(self.timeout)

            while time() - startTime < self.timeout:
                # Sample another group of data
                size = random.choice(range(self.lower, self.upper + 1))
                startingPoint = choice(range(len(self.data) - size + 1))
                endingPoint = startingPoint + size
                subset = self.data[startingPoint:endingPoint]

                if self.dummy:
                    print "Not actually doing ransac, but if I were this is the data I would use:"
                    for xs in subset:
                        print "\t".join("".join(x.phonemes) for x in xs)
                    break

                n0 = min(6,size)
                morphology = Solution(rules = [],
                                      prefixes = [Morph([])]*2,
                                      suffixes = [Morph([]),Morph([u'ə'])])
                try:
                    worker = self.restrict(subset)
                    if False:# do straight up CEGIS
                        solutions += worker.counterexampleSolution(initialTrainingSize = n0,
                                                                   fixedMorphology = morphology,
                                                                   k = 1,
                                                                   maximumDepth = 2,
                                                                   initialDepth = 2)
                    else:
                        solutions += worker.incrementallySolve(fixedMorphology = morphology)
                except SynthesisTimeout: break

            flushEverything()
            return [ s.clearTransducers() for s in solutions ]
        except Exception as e:
            print "Exception in worker:", traceback.format_exc()
            flushEverything()
            return [ s.clearTransducers() for s in solutions ]

    def solve(self, numberOfWorkers = None, numberOfSamples = 50):
        if numberOfWorkers == None: numberOfWorkers = numberOfCPUs()
        print "# of workers:",numberOfWorkers
        if numberOfWorkers > 1:
            solutions = Pool(numberOfWorkers).map(lambda j: self.worker(j), range(numberOfSamples))
        else:
            solutions = map(lambda j: self.worker(j), range(numberOfSamples))
            setGlobalTimeout(None)
            
        # Now coalesce the rules and figure out how frequently they occurred
        ruleFrequencies = {} # map from the Unicode representation of a rule to (frequency,rule)
        for r in [ r for ss in solutions for s in ss for r in s.rules ]:
            (oldFrequency,_) = ruleFrequencies.get(unicode(r), (0,r))
            ruleFrequencies[unicode(r)] = (oldFrequency + 1, r)

        print "Most popular rules..."
        for f,r in sorted(ruleFrequencies.values(), key = lambda fr: fr[0]):
            print f,"\t",r.pretty()

        return 
        
        # Now coalesce the morphologies and figure out how frequently those occurred
        morphologyFrequencies = {} # map from (frequency, prefixes, suffixes)
        for s in [ s for ss in solutions for s in ss ]:
            k = tuple([ unicode(m) for m in s.prefixes + s.suffixes ])
            (oldFrequency, oldValue) = morphologyFrequencies.get(k, (0,s.prefixes,s.suffixes))
            morphologyFrequencies[k] = (oldFrequency + 1, oldValue)
            
        for f, prefixes, suffixes in sorted(morphologyFrequencies.keys(), key = lambda fr: fr[0]):
            print f
            for p,s in zip(prefixes, suffixes):
                print p,'+stem+',s
            print 
        
