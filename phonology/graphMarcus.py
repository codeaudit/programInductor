from Marcus import *
from fragmentGrammar import *
from utilities import *

from collections import defaultdict

import os
import random

from matplotlib.lines import Line2D
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plot
import matplotlib.pylab as pylab

pylab.rcParams.update({'axes.labelsize': 14,
                       'xtick.labelsize': 12,
                       'ytick.labelsize': 12})

BANK = None

transductionCashFile = ".MarcusTransductionTable.p"

TRANSDUCTIONTABLE = {}
def cachedTransduction(s, word):
    global TRANSDUCTIONTABLE, BANK
    key = (s.withoutStems(),
           word)
    if key in TRANSDUCTIONTABLE:
        return TRANSDUCTIONTABLE[key]
    TRANSDUCTIONTABLE[key] = s.transduceUnderlyingForm(BANK,(Morph(word),))
    return TRANSDUCTIONTABLE[key]

def solutionJoint(solution):
    b = FeatureBank(list({ s
                          for ss in solution.underlyingForms.keys()
                           for s in ss } | {u"-"}))
    getEmptyFragmentGrammar().numberOfFeatures = len(b.features)
    getEmptyFragmentGrammar().numberOfPhonemes = len(b.phonemes)    

    lexicon = -sum(len(stem) for stem in solution.underlyingForms.values() )
    morphology = -sum(len(stem) for stem in solution.suffixes + solution.prefixes)
    rules = sum(getEmptyFragmentGrammar().ruleLogLikelihood(r)[0]
                for r in solution.rules)
    rules_symbols = -sum(r.cost() for r in solution.rules)

    return math.log(len(b.phonemes))*(lexicon + morphology) + rules/5

def calculatePosterior(solutions):
    # compute posterior probabilities for each element in posterior
    logPosterior = [solutionJoint(solution) for solution in solutions ]
    z = lseList(logPosterior)
    logPosterior = [lp - z for lp in logPosterior ]

    return list(sorted(zip(solutions, logPosterior), key=lambda sp: -sp[1]))

def posteriorPredictiveLikelihood(solutions, testWord):
    b = FeatureBank([ s
                      for solution in solutions
                      for ss in solution.underlyingForms.keys()
                      for s in ss ] + [u"-"])

    logMarginal = float('-inf')
    for solution, lp in calculatePosterior(solutions):
        stem = cachedTransduction(solution, testWord)
        if stem is None: continue

        logMarginal = lse(logMarginal, lp - len(stem)*math.log(len(b.phonemes)))

    return logMarginal    
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Analyze and plot Marcus patterns on held out data')
    pairings = ["%s,%s"%(x,y)
                for x in ["aba","aab","abb","abx","aax","Chinese","axa"]
                for y in ["aba","aab","abb","abx","aax","Chinese","axa"]
                if x != y]
    parser.add_argument('testCases',
                        choices = pairings,
                        type = str,
                        nargs='+')
    parser.add_argument('--colors',
                        type = str,
                        default=None,
                        nargs='+')
    parser.add_argument('-n','--number', default = 4, type = int)
    parser.add_argument('-s','--samples', default=1, type=int)
    parser.add_argument('--sigmoid', default=False, type=float,
                        help="Plot sigmoid(log-odds/T), --sigmoid T ")
    parser.add_argument('--deviation', default=1., type=float,
                        help="scales the error bars by this factor.")
    parser.add_argument('-j','--jitter', default=0., type=float)
    parser.add_argument('--export', default = None, type = str)
    parser.add_argument('--debug', default = False, action='store_true')

    random.seed(0)

    if os.path.exists(transductionCashFile):
        print "Loading transductions from",transductionCashFile
        TRANSDUCTIONTABLE = loadPickle(transductionCashFile)
    
    arguments = parser.parse_args()

    arguments.testCases = [tuple(tc.split(","))
                           for tc in arguments.testCases ]
    
    withSyllables = {} # map from (training distribution, n_examples) to [solution]
    withoutSyllables = {} # map from (training distribution, n_examples) to [solution]
    consistentExamples = {} # map from (consistent, inconsistent) distribution to consistent test examples
    inconsistentExamples = {} # map from (consistent, inconsistent) to inconsistent test examples
    jobs = set() # {(solution, word)}
    everyWord = set() # set of every word ever
    for consistent, inconsistent in arguments.testCases:
        allTrainingExamples = set()
        X = None
        for n in range(1,arguments.number+1):
            withSyllables[consistent,n] = loadPickle("paretoFrontier/%s%d.p"%(consistent,n)).values()
            withoutSyllables[consistent,n] = loadPickle("paretoFrontier/%s%d_noSyllable.p"%(consistent,n)).values()
        
            # Control for training data
            surfaces1 = set(withSyllables[consistent,n][0].underlyingForms.keys())
            surfaces2 = set(withoutSyllables[consistent,n][0].underlyingForms.keys())
            for surface in surfaces1|surfaces2:
                allTrainingExamples.add(surface[0])
            assert len(surfaces1^surfaces2) == 0

            # Figure out what X is
            if consistent in {'abx','aax'}:
                X = u"".join(withSyllables[consistent,n][0].underlyingForms.keys()[0][0].phonemes[-2:])
            elif consistent == 'axa':
                X = u"".join(withSyllables[consistent,n][0].underlyingForms.keys()[0][0].phonemes[2:][:2])
        print consistent, inconsistent, "\tX=",X
    
        sampling = {'aba': sampleABA,
                    'abb': sampleABB,
                    'abx': lambda ne: sampleABX(ne,X=X),
                    'aax': lambda ne: sampleAAX(ne,X=X),
                    'axa': lambda ne: sampleAXA(ne,X=X),
                    'aab': sampleAAB,
                    }    
        random.seed(0)
        testConsistent = []
        while len(testConsistent) < arguments.samples:
            w = Morph(sampling[consistent](1)[0])
            if w not in allTrainingExamples: testConsistent.append(w)

        random.seed(0)
        testInconsistent = []
        while len(testInconsistent) < arguments.samples:
            w = Morph(sampling[inconsistent](1)[0])
            # If we train on e.g. aax, and test on aab, make sure that it doesn't accidentally conform to the training pattern
            if 'x' in consistent and 'x' not in inconsistent:
                if X in u"".join(w.phonemes): continue
            
            if w not in allTrainingExamples: testInconsistent.append(w)

        for n in range(1,arguments.number+1):
            for s in withSyllables[consistent,n] + withoutSyllables[consistent,n]:
                for surfaces in s.underlyingForms.keys():
                    for surface in surfaces: everyWord.add(surface)
                for test in testConsistent + testInconsistent:
                    everyWord.add(Morph(test))
                    jobs.add((s.withoutStems(), test))

        consistentExamples[consistent,inconsistent] = testConsistent
        inconsistentExamples[consistent,inconsistent] = testInconsistent

    BANK = FeatureBank([u"-"] + list(everyWord))

    # Batched likelihood calculation in parallel
    transductions = \
                    lightweightParallelMap(numberOfCPUs(), 
                                           lambda (s,w): (s,w,s.transduceUnderlyingForm(BANK,(w,))),
                                           list(jobs - set(TRANSDUCTIONTABLE.keys())))
    for solution, word, transduction in transductions:
        TRANSDUCTIONTABLE[(solution, word)] = transduction

    if len(transductions) > 0:
        print "Updating cached transductions in",transductionCashFile
        temporaryFile = makeTemporaryFile(".p")
        dumpPickle(TRANSDUCTIONTABLE, temporaryFile)
        os.system("mv %s %s"%(temporaryFile, transductionCashFile))
    

    
    plot.figure(figsize=(8,3))
    xs = range(0,arguments.number+1)
    COLORS = arguments.colors or ["r","g","b","cyan"]

    random.seed() # use the current time for jittering
    for color, (consistent, inconsistent) in zip(COLORS,arguments.testCases):
        if arguments.debug:
            for n in range(1,arguments.number+1):
                print("After training on %d examples w/ syllables, posterior is:"%(n))
                for s,lp in calculatePosterior(withSyllables[consistent,n]):
                    print("Posterior probability",lp)
                    print(s)
                    for e in consistentExamples[consistent, inconsistent]:
                        print("consistent\tlog P(%s | theory) = %s"%(e,cachedTransduction(s,e)))
                    for e in inconsistentExamples[consistent, inconsistent]:
                        print("inconsistent\tlog P(%s | theory) = %s"%(e,cachedTransduction(s,e)))
            
                    
            
        for syllables in [withoutSyllables, withSyllables]:
            ys = [0.5] if sigmoid else [0]
            deviations = [0]
            for n in range(1,arguments.number+1):
                # with syllables after n examples
                consistentLikelihoods = \
                 [posteriorPredictiveLikelihood(syllables[consistent,n], e)
                 for e in consistentExamples[consistent, inconsistent] ]
                inconsistentLikelihoods = \
                 [posteriorPredictiveLikelihood(syllables[consistent,n], e)
                 for e in inconsistentExamples[consistent, inconsistent] ]
                y = average(consistentLikelihoods) - average(inconsistentLikelihoods)
                if arguments.sigmoid:
                    y = sigmoid(y/arguments.sigmoid)
                    s = standardDeviation([sigmoid((c - i)/arguments.sigmoid)
                                           for c in consistentLikelihoods
                                           for i in inconsistentLikelihoods ])
                else:
                    s = standardDeviation([c - i
                                           for c in consistentLikelihoods
                                           for i in inconsistentLikelihoods ])

                ys.append(y)

                deviations.append(s*arguments.deviation)
            jxs = [x + arguments.jitter*(2*(random.random() - 0.5))
                   for x in xs ]
            if len(arguments.testCases) > 1:
                plot.errorbar(jxs,ys,yerr=deviations,color=color,
                              ls='--' if syllables is withSyllables else ':',
                              linewidth=5 if syllables is withSyllables else 3,
                              alpha=0.9)
            else:
                plot.errorbar(jxs,ys,yerr=deviations,
                              color=COLORS[int(syllables is withSyllables)])

    
    plot.xlabel("# training examples")
    plot.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    if arguments.sigmoid:
        plot.ylim(bottom=0.,top=1.1)
        if False and abs(arguments.sigmoid - 1) > 0.1:
            plot.ylabel(r"$\sigma(1/%i\times\log\frac{\mathrm{P}(\mathrm{consistent}|\mathrm{train})}{\mathrm{P}(\mathrm{inconsistent}|\mathrm{train})})$"%(int(arguments.sigmoid)))
        else:
            plot.ylabel(r"$\sigma(\log\frac{\mathrm{P}(\mathrm{consistent}|\mathrm{train})}{\mathrm{P}(\mathrm{inconsistent}|\mathrm{train})})$")
    else:
        plot.ylabel(r"$\log\frac{\mathrm{P}(\mathrm{consistent}|\mathrm{train})}{\mathrm{P}(\mathrm{inconsistent}|\mathrm{train})}$")
    if len(arguments.testCases) > 1:
        plot.legend([Line2D([0],[0],color=c,lw=2)
                     for c,_ in zip(COLORS,arguments.testCases)] + \
                    [Line2D([0],[0],color='k',lw=5,ls='--'),
                     Line2D([0],[0],color='k',lw=3,ls=':')],
                    ["train %s, test %s (consistent) / %s (inconsistent)"%(c,c,i)
                     for c,i in arguments.testCases ] + \
                    ["w/ syllables", "w/o syllables"],
                    ncol=2,
                    loc='lower center',#                    loc='best',
                    fontsize=8)
    else:
        c = arguments.testCases[0][0]
        i = arguments.testCases[0][1]
        plot.title("train %s, test %s (consistent) / %s (inconsistent)"%(c,c,i))
        plot.legend([Line2D([0],[0],color=COLORS[1],lw=2),
                     Line2D([0],[0],color=COLORS[0],lw=2)],
                    ["w/ syllables", "w/o syllables"],
                    ncol=2,
                    loc='best')

    if arguments.export:
        plot.tight_layout()        
        plot.savefig(arguments.export)
    else:
        plot.show()
