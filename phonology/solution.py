from sketchSyntax import *
from sketch import *
from utilities import *
from rule import *
from features import *
from compileRuleToSketch import compileRuleToSketch

from Panini import *

class Solution():
    def __init__(self,rules = [],prefixes = [],suffixes = [],underlyingForms = [],adjustedCost = None):
        assert len(prefixes) == len(suffixes)
        self.rules = rules
        self.prefixes = prefixes
        self.suffixes = suffixes
        self.underlyingForms = underlyingForms
        self.adjustedCost = adjustedCost

    def __str__(self):
        return "\n".join([ "rule: %s"%(str(r)) for r in self.rules ] +
                         [ "%s + stem + %s"%(str(self.prefixes[j]),str(self.suffixes[j]))
                           for j in range(len(self.prefixes)) ] +
                         (["underlying form: %s"%str(u)
                           for u in self.underlyingForms ]))

    def cost(self):
        return sum([ r.cost() for r in self.rules ] +
                   [ len(s) for s in (self.prefixes + self.suffixes + self.underlyingForms) ])

    def modelCost(self):
        return sum([ r.cost() for r in self.rules ] +
                   [ len(s) for s in (self.prefixes + self.suffixes) ])

    def depth(self): return len(self.rules)

    def showMorphologicalAnalysis(self):
        print "Morphological analysis:"
        for i in range(len(self.prefixes)):
            print "Inflection %d:\t"%i,
            print self.prefixes[i],
            print "+ stem +",
            print self.suffixes[i]

    def showRules(self):
        print "Phonological rules:"
        for r in self.rules: print r

    def mutate(self,bank):
        # mutate a phoneme
        if random() < 0.3:
            newPrefixes = list(self.prefixes)
            newSuffixes = list(self.suffixes)
            for _ in range(sampleGeometric(0.7) + 1):
                i = choice(range(len(self.prefixes)))
                if choice([True,False]): # mutate a prefix
                    newPrefixes[i] = newPrefixes[i].mutate(bank)
                else:
                    newSuffixes[i] = newSuffixes[i].mutate(bank)
            return Solution(self.rules,newPrefixes,newSuffixes)
                
        # mutate a rule
        if random() < 0.5:
            r = choice(self.rules)
            newRules = [ (r.mutate(bank) if q == r else q) for q in self.rules ]
            return Solution(newRules,self.prefixes,self.suffixes)
        # reorder the rules
        if len(self.rules) > 1 and random() < 0.3:
            i = choice(range(len(self.rules)))
            j = choice([ k for k in range(len(self.rules)) if k != i ])
            newRules = [ self.rules[i if k == j else (j if k == i else k)]
                         for k in range(len(self.rules)) ]
            return Solution(newRules,self.prefixes,self.suffixes)
        # delete a rule
        if len(self.rules) > 1 and random() < 0.3:
            newRules = randomlyRemoveOne(self.rules)
            return Solution(newRules,self.prefixes,self.suffixes)
        # insert a rule
        newRules = list(self.rules)
        newRules.insert(choice(range(len(self.rules)+1)), EMPTYRULE.mutate(bank).mutate(bank).mutate(bank).mutate(bank))
        return Solution(newRules,self.prefixes,self.suffixes)
        
    def phonologyTransducer(self,bank):
        return reduce(lambda p,q: p*q, [r.fst(bank) for r in self.rules])

    def withoutUselessRules(self):
        return Solution(prefixes = self.prefixes,
                        suffixes = self.suffixes,
                        underlyingForms = self.underlyingForms,
                        rules = [ r for r in self.rules
                                  if len(self.rules) == 1 or (not r.doesNothing()) ],
                        adjustedCost = self.adjustedCost)

    def morphologyTransducers(self, bank):
        def makeTransducer(prefix, suffix):
            return\
                transducerOfRule({'': suffix.fst(bank)}, '', '[EOS]', bank.transducerAlphabet())*\
                transducerOfRule({'': prefix.fst(bank)}, '[BOS]', '', bank.transducerAlphabet())

        return [ makeTransducer(prefix, suffix) for prefix, suffix in zip(self.prefixes, self.suffixes) ]

    def inflectionTransducers(self, bank):
        if not hasattr(self,'savedInflectionTransducers'):
            phonology = self.phonologyTransducer(bank)
            self.savedInflectionTransducers = [ m*phonology for m in self.morphologyTransducers(bank) ]
        return self.savedInflectionTransducers

    def clearTransducers(self):
        if hasattr(self,'savedInflectionTransducers'): del self.savedInflectionTransducers
        return self

    def transduceUnderlyingForm(self, bank, surfaces):
        '''surfaces: list of morphs'''
        try:
            transducers = self.inflectionTransducers(bank)
        except InvalidRule as ex:
            print "INVALIDRULE???"
            print ex
            return None

        applicableTransducersAndSurfaces = [ (s.fst(bank),t)
                                             for (t,s) in zip(transducers, surfaces) if s != None ]

        ur = parallelInversion(applicableTransducersAndSurfaces)
        if ur == None: return None
        return Morph([ bank.fst2phoneme(p) for p in ur ])

    def verifyRuleCompilation(self, b, data):
        Model.Global()

        rules = [ compileRuleToSketch(b,r) for r in self.rules ]

        for i in range(len(self.prefixes)):
            for j in range(len(data)):
                ur = self.prefixes[i] + self.underlyingForms[j] + self.suffixes[i]
                ur = ur.makeConstant(b)
                condition(wordEqual(data[j][i].makeConstant(b),
                                    applyRules(rules, ur, None)))
        if solveSketch(b,unroll = 15,maximumMorphLength = 15) == None:
            print "Could not verify rule compilation:"
            print self
            printSketchFailure()
            for o,u in zip(data,self.underlyingForms):
                print o,'is underlyingly ',u
            assert False
            
