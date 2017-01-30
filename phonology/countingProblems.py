# -*- coding: utf-8 -*-

from features import FeatureBank, tokenize
from rule import *
from morph import Morph
from sketch import *


class CountingProblem():
    def __init__(self, data, count):
        self.data = data
        self.count = count
        self.bank = FeatureBank([ w for w in data ])

        self.maximumObservationLength = max([ len(tokenize(w)) for w in data ]) + 1

    def topSolutions(self, k = 10):
        solutions = []
        for _ in range(k):
            r = self.sketchSolution(solutions)
            if r == None: break
            solutions.append(r)
        return solutions

    def sketchSolution(self, existingRules):
        Model.Global()

        r = Rule.sample()
        for o in existingRules:
            condition(ruleEqual(r, o.makeConstant(self.bank)) == 0)

        morphs = {}
        morphs[1] = Morph.sample()
        morphs[4] = Morph.sample()
        morphs[5] = Morph.sample()
        morphs[9] = Morph.sample()
        morphs[10] = Morph.sample()

        # intended = Rule(FeatureMatrix([(False,'vowel')]),
        #                 EmptySpecification(),
        #                 Guard('L', True, False, []),
        #                 Guard('R', False, False, [FeatureMatrix([(False,'vowel')])]))
#        condition(ruleEqual(r,intended.makeConstant(self.bank)))

        for j in range(len(self.data)):
            o = self.data[j]
            k = self.count[j]
            if k <= 10:
                condition(wordEqual(makeConstantWord(self.bank, o),
                                    applyRule(r,morphs[k])))
            elif k%10 == 0:
                condition(wordEqual(makeConstantWord(self.bank, o),
                                    applyRule(r,concatenate(morphs[k/10], morphs[10]))))
            elif k < 20:
                condition(wordEqual(makeConstantWord(self.bank, o),
                                    applyRule(r,concatenate(morphs[10], morphs[k - 10]))))
            else:
                assert False

        minimize(ruleCost(r))

        output = solveSketch(self.bank, self.maximumObservationLength)
        
        if not output:
            print "Failed at phonological analysis."
            return None

        r = Rule.parse(self.bank, output, r)
        print r
        return r
