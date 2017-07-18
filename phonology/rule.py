# -*- coding: utf-8 -*-

from problems import interactingProblems
from sketchSyntax import define, FunctionCall, Constant
from features import FeatureBank,featureMap,tokenize
from latex import latexWord
from morph import Morph
from utilities import *

from Panini import *

import re
from random import choice,random
import numpy as np
import itertools

class InvalidRule(Exception):
    pass

class Braces():
    '''
SPE-style brackets for rule alternatives.
'''
    def __init__(self, r1,r2):
        self.r1 = r1
        self.r2 = r2

    def __unicode__(self):
        return u"{ " + unicode(self.r1) + u" || " + unicode(self.r2) + u" }"
    def __str__(self): return unicode(self).encode('utf-8')
    def latex(self):
        return "\\verb|{ | %s \\verb| , | %s \\verb|}|"%(self.r1.latex(),self.r2.latex())
    def cost(self):
        k = self.r1.cost() + self.r2.cost()
        # do not incur cost of repeating exactly the same structure
        if isinstance(self.r1,ConstantPhoneme) and isinstance(self.r2,ConstantPhoneme):
            k -= 1
        if isinstance(self.r1,FeatureMatrix) and isinstance(self.r2,FeatureMatrix):
            k -= 1
        return k



class Specification():
    def __init__(self): pass

    @staticmethod
    def sample(bank, canBeEmpty = False):
        if canBeEmpty and random() < 0.3:
            return EmptySpecification()

        if choice([True,False]):
            return ConstantPhoneme(choice(bank.phonemes))
        else:
            numberOfFeatures = min(len(bank.features),sampleGeometric(0.5))
            return FeatureMatrix([ (choice([True,False]),f)
                                   for f in np.random.choice(bank.features,size = numberOfFeatures,replace = False) ])

    
    @staticmethod
    def parse(bank, output, variable):
        try:
            return FeatureMatrix.parse(bank, output, variable)
        except:
            try:
                return EmptySpecification.parse(bank, output, variable)
            except:
                return ConstantPhoneme.parse(bank, output, variable)

    @staticmethod
    def enumeration(b,cost):
        return ConstantPhoneme.enumeration(b,cost) + FeatureMatrix.enumeration(b,cost)
        
class ConstantPhoneme(Specification):
    def __init__(self, p): self.p = p
    def __unicode__(self):
        if self.p == '-': return u"syl"
        else:
            return self.p
    def __str__(self): return unicode(self).encode('utf-8')
    def doesNothing(self): return False
    def cost(self): return 2
    def skeleton(self): return "K"
    def latex(self): return latexWord(self.p)
    def fst(self,bank):
        return [bank.phoneme2fst(self.p)]
    def mutate(self,bank): return ConstantPhoneme(choice(bank.phonemes))

    def share(self, table):
        k = ('CONSTANT',unicode(self))
        if k in table: return table[k]
        table[k] = self
        return self

    def merge(self, other):
        if isinstance(other, ConstantPhoneme) and other.p == self.p: return self
        return Braces(self, other)
    
    @staticmethod
    def parse(bank, output, variable):
        pattern = " %s = new ConstantPhoneme\(phoneme=phoneme_([0-9]+)_" % str(variable)
        m = re.search(pattern, output)
        if not m: raise Exception('Failure parsing ConstantPhoneme %s, pattern = %s'%(variable,pattern))
        return ConstantPhoneme(bank.phonemes[int(m.group(1))])
    def makeConstant(self, bank):
        return "new ConstantPhoneme(phoneme = phoneme_%d)" % bank.phoneme2index[self.p]

    def matches(self, test):
        return set(featureMap[self.p]) == set(test)
    def apply(self, test):
        return featureMap[self.p]

    @staticmethod
    def enumeration(b,cost):
        if cost > 1: return [ConstantPhoneme(p) for p in b.phonemes ]
        return []

    def extension(self,b): return [self.p]

class EmptySpecification():
    def __init__(self): pass
    def __unicode__(self): return u"Ø"
    def __str__(self): return unicode(self).encode('utf-8')

    def doesNothing(self): return False
    def skeleton(self): return "0"
    def cost(self): return 2
    def latex(self): return '$\\varnothing$'
    def mutate(self,_): return self

    def share(self, table):
        k = ('EMPTYSPECIFICATION',unicode(self))
        if k in table: return table[k]
        table[k] = self
        return self

    def merge(self, other):
        if isinstance(other, EmptySpecification): return self
        return Braces(self, other)

    @staticmethod
    def parse(bank, output, variable):
        pattern = " %s = null;" % variable
        m = re.search(pattern, output)
        if not m: raise Exception('Failure parsing empty specification %s'%variable)
        return EmptySpecification()
    def makeConstant(self, bank):
        return "null"

    def matches(self, test):
        return True
    def apply(self, test):
        raise Exception('cannot apply deletion rule')
    
class FeatureMatrix():
    def __init__(self, featuresAndPolarities):
        self.featuresAndPolarities = featuresAndPolarities
        self.representation = None # string representation

    def mutate(self, bank):
        # delete a feature
        if self.featuresAndPolarities != [] and random() < 0.5:
            toRemove = choice(self.featuresAndPolarities)
            return FeatureMatrix([ fp for fp in self.featuresAndPolarities if fp != toRemove ])
        else:
            fp = (choice([True,False]),choice(bank.features))
            return FeatureMatrix(list(set(self.featuresAndPolarities + [fp])))
            
        
    @staticmethod
    def strPolarity(p): return '+' if p == True else ('-' if p == False else p)
    def __str__(self): return unicode(self).encode('utf-8')
    def __unicode__(self):
        if not hasattr(self, 'representation') or self.representation == None:
            elements = sorted([ FeatureMatrix.strPolarity(polarity)+f for polarity,f in self.featuresAndPolarities ])
            self.representation = u"[ {} ]".format(u" ".join(elements))
        return self.representation

    def doesNothing(self):
        return len(self.featuresAndPolarities) == 0

    def cost(self):
        return 1 + len(self.featuresAndPolarities)

    def skeleton(self):
        if self.featuresAndPolarities == []: return "[ ]"
        else: return "[ +/-F ]"

    def fst(self,bank):
        # which phonemes in the bank does this refer to?
        setOfPhonemes = [ bank.phoneme2fst(p)
                          for p in bank.phonemes
                          if self.matches(featureMap[p]) ]
        if len(setOfPhonemes) == 0: raise InvalidRule('FeatureMatrix: %s'%str(self))
        return setOfPhonemes

    def latex(self):
        if self.featuresAndPolarities == []: return '\\verb|[ ]|'
        return '\\verb|[%s]|'%(" ".join([ ('+' if polarity else '-')+f for polarity,f in self.featuresAndPolarities ]))

    def share(self, table):
        k = ('MATRIX',unicode(self))
        if k in table: return table[k]
        table[k] = self
        return self

    def merge(self, other):
        if isinstance(other, FeatureMatrix):
            if set([f for _,f in self.featuresAndPolarities ]) == set([f for _,f in other.featuresAndPolarities ]):
                # introduce feature variables
                y = dict([(f,p) for p,f in self.featuresAndPolarities ])
                x = dict([(f,p) for p,f in other.featuresAndPolarities ])
                fs = [ (x[f] if x[f] == y[f] else
                        FeatureMatrix.strPolarity(x[f])+'/'+FeatureMatrix.strPolarity(y[f]), f) for f in y ]
                return FeatureMatrix(fs)
        
        return Braces(self, other)

    @staticmethod
    def parse(bank, output, variable):
        pattern = " %s = new Vector\(mask={([01,]+)}, preference={([01,]+)}"%variable
        m = re.search(pattern, output)
        if not m: raise Exception('Failure parsing Vector %s'%variable)
        preference = [ int(x) for x in m.group(2).split(",") ]
        mask = [ int(x) for x in m.group(1).split(",") ]
        fs = [ (preference[f] == 1, bank.features[f]) for f in range(len(bank.features)) if mask[f] ]
        return FeatureMatrix(fs)
    def makeConstant(self, bank):
        mask = [0]*len(bank.features)
        preference = [0]*len(bank.features)
        for polarity,feature in self.featuresAndPolarities:
            mask[bank.feature2index[feature]] = 1
            preference[bank.feature2index[feature]] = 1 if polarity else 0
        mask = " ,".join(map(str, mask))
        preference = " ,".join(map(str, preference))
        return "new Vector(mask = {%s}, preference = {%s})" % (mask, preference)

    def matches(self, test):
        for p,f in self.featuresAndPolarities:
            if p:
                if not (f in test): return False
            else:
                if f in test: return False
        return True
    def extension(self,bank):
        return [p for p in bank.phonemes if self.matches(featureMap[p]) ]
    def apply(self, test):
        for p,f in self.featuresAndPolarities:
            if p:
                test = test + [f]
                # mutually exclusive features
                for k in FeatureBank.mutuallyExclusiveClasses:
                    if f in k:
                        test = [_f for _f in test if ((not _f in k) or _f == f) ]
                        # Assumption: exclusive classes are themselves mutually exclusive
                        break            
            else:
                test = [_f for _f in test if not _f == f ]
        return list(set(test))

    @staticmethod
    def enumeration(b,cost):
        if cost < 1: return []
        cost -= 1
        results = []
        for k in range(cost + 1):
            for features in itertools.combinations(b.features,k):
                for polarities in itertools.product(*([(True,False)]*k)):
                    results.append(FeatureMatrix(zip(polarities, features)))
        return results
            

class Guard():
    def __init__(self, side, endOfString, starred, specifications):
        self.side = side
        self.endOfString = endOfString
        self.starred = starred
        self.specifications = [ s for s in specifications if s != None ]
        self.representation = None # Unicode representation

    def mutate(self,bank):
        endOfString = self.endOfString
        if random() < 0.15: endOfString = not endOfString

        specifications = [ (s if random() < 0.9 else s.mutate(bank)) for s in self.specifications ]
        # with some small probability remove a specification
        if specifications != [] and random() < 0.1:
            specifications = randomlyRemoveOne(specifications)
        # with the same probability adding specification
        elif len(specifications) < 2 and random() < 0.1:
            if choice([True,False]): specifications = specifications + [Specification.sample(bank)]
            else: specifications = [Specification.sample(bank)] + specifications

        starred = self.starred
        if random() < 0.1: starred = not starred
        if len(specifications) < 2: starred = False

        return Guard(self.side, endOfString, starred, specifications)

    @staticmethod
    def sample(bank,side):
        numberOfSpecifications = choice([0,1,2])
        return Guard(side,
                     choice([True,False]),
                     choice([True,False]) and numberOfSpecifications == 2,
                     [ Specification.sample(bank) for _ in range(numberOfSpecifications) ])

    def doesNothing(self):
        return not self.endOfString and len(self.specifications) == 0

    def cost(self):
        return int(self.starred) + int(self.endOfString) + sum([ s.cost() for s in self.specifications ])
    
    def __str__(self): return unicode(self).encode('utf-8')
    def __unicode__(self):
        if not hasattr(self, 'representation') or self.representation == None:
            parts = []
            parts += map(unicode,self.specifications)
            if self.starred: parts[-2] += u'*'
            if self.endOfString: parts += [u'#']
            if self.side == 'L': parts.reverse()
            self.representation = u" ".join(parts)
        return self.representation
    
    def skeleton(self):
        parts = []
        parts += map(lambda spec: spec.skeleton(),self.specifications)
        if self.starred: parts[-2] += '*'
        if self.endOfString: parts += ['#']
        if self.side == 'L': parts.reverse()
        return " ".join(parts)
    def latex(self):
        parts = []
        parts += map(lambda spec: spec.latex(),self.specifications)
        if self.starred: parts[-2] += '*'
        if self.endOfString: parts += ['#']
        if self.side == 'L': parts.reverse()
        return " ".join(parts)

    def fst(self,bank):
        parts = [ unionTransducer(s.fst(bank)) for s in self.specifications ]
        if self.starred: parts[-2] = parts[-2].closure()
        if self.endOfString: parts += ['[EOS]' if self.side == 'R' else '[BOS]']
        if self.side == 'L': parts.reverse()
        if parts == []: return ""
        t = parts[0]
        parts = parts[1:]
        while parts != []:
            t = t + parts[0]
            parts = parts[1:]
        return t

    def share(self, table):
        k = ('GUARD',self.side,unicode(self))
        if k in table: return table[k]
        table[k] = Guard(self.side, self.endOfString, self.starred,
                         [s.share(table) for s in self.specifications ])
        return table[k]

    def merge(self, other):
        assert other.side == self.side
        if self.endOfString != other.endOfString or self.starred != other.starred or len(self.specifications) != len(other.specifications):
            return Braces(self, other)
        return Guard(self.side,
                     self.endOfString,
                     self.starred,
                     [ x.merge(y) for x,y in zip(self.specifications,other.specifications) ])

    @staticmethod
    def parse(bank, output, variable, side):
        pattern = " %s = new Guard\(endOfString=([01]), starred=([01]), spec=([a-zA-Z0-9_]+), spec2=([a-zA-Z0-9_]+)"%variable
        m = re.search(pattern, output)
        if not m: raise Exception('Could not parse guard %s using pattern %s'%(variable,pattern))

        endOfString = m.group(1) == '1'
        starred = m.group(2) == '1'
        spec = None if m.group(3) == 'null' else Specification.parse(bank, output, m.group(3))
        spec2 = None if m.group(4) == 'null' else Specification.parse(bank, output, m.group(4))
        return Guard(side, endOfString, starred, [spec,spec2])
    def makeConstant(self, bank):
        if len(self.specifications) == 2:
            [spec1,spec2] = self.specifications
            spec1 = self.specifications[0].makeConstant(bank)
            spec2 = self.specifications[1].makeConstant(bank)
        elif len(self.specifications) == 1:
            spec1 = self.specifications[0].makeConstant(bank)
            spec2 = "null"
        else:
            spec1 = "null"
            spec2 = "null"
        
        return "new Guard(endOfString = %d, starred = %d, spec = %s, spec2 = %s)" % (1 if self.endOfString else 0,
                                                                                     1 if self.starred else 0,
                                                                                     spec1,
                                                                                     spec2)

    @staticmethod
    def enumeration(side,b,cost):
        results = []
        for ending in [False,True]:
            for numberOfSpecifications in range(3):
                for starred in ([False] if numberOfSpecifications < 2 else [True,False]):
                    if numberOfSpecifications == 0:
                        if int(starred) + int(ending) <= cost: results.append(Guard(side,ending,starred,[]))
                    elif numberOfSpecifications == 1:
                        for s in Specification.enumeration(b,cost - int(starred) - int(ending)):
                            results.append(Guard(side,ending,starred,[s]))
                    elif numberOfSpecifications == 2:
                        for s1 in Specification.enumeration(b,cost - int(starred) - int(ending)):
                                for s2 in Specification.enumeration(b,cost - int(starred) - int(ending) - s1.cost()):
                                    results.append(Guard(side,ending,starred,[s1,s2]))
                    else: assert False
        return results
    
class Rule():
    SAVEDTRANSDUCERS = {}
    
    def __init__(self, focus, structuralChange, leftTriggers, rightTriggers, copyOffset):
        self.focus = focus
        self.structuralChange = structuralChange
        self.leftTriggers = leftTriggers
        self.rightTriggers = rightTriggers
        self.copyOffset = copyOffset
        self.representation = None # Unicode representation

    def merge(self, other):
        return Rule(self.focus.merge(other.focus),
                    self.structuralChange.merge(other.structuralChange),
                    self.leftTriggers.merge(other.leftTriggers),
                    self.rightTriggers.merge(other.rightTriggers),
                    self.copyOffset if self.copyOffset == other.copyOffset else Braces(self.copyOffset,other.copyOffset))
                    
    def share(self, table):
        k = ('RULE',unicode(self))
        if k in table: return table[k]
        table[k] = Rule(self.focus.share(table),
                        self.structuralChange.share(table),
                        self.leftTriggers.share(table),
                        self.rightTriggers.share(table),
                        self.copyOffset)
        return table[k]

    def cost(self):
        return self.focus.cost() + self.structuralChange.cost() + self.leftTriggers.cost() + self.rightTriggers.cost()
    def alternationCost(self):
        return self.leftTriggers.cost() + self.rightTriggers.cost()   

    def doesNothing(self):
        '''Does this rule do nothing? Equivalently is it [  ] ---> [  ] /  _ '''
        return self.leftTriggers.doesNothing() and self.rightTriggers.doesNothing() and self.focus.doesNothing() and self.structuralChange.doesNothing()

    def __str__(self): return unicode(self).encode('utf-8')
    def __unicode__(self):
        if not hasattr(self, 'representation') or self.representation == None:
            if not hasattr(self, 'copyOffset'): self.copyOffset = 0
            # check this: should I be calling Unicode recursively?
            self.representation = u"{} ---> {} / {} _ {}".format(unicode(self.focus),
                                                                 unicode(self.structuralChange) if self.copyOffset == 0 else self.copyOffset,
                                                                 unicode(self.leftTriggers),
                                                                 unicode(self.rightTriggers))
        return self.representation
    
    def skeleton(self):
        return "{} ---> {} / {} _ {}".format(self.focus.skeleton(),
                                             self.structuralChange.skeleton(),
                                             self.leftTriggers.skeleton(),
                                             self.rightTriggers.skeleton())
    def latex(self):
        return "{} $\\to$ {} / {} \\verb|_| {}".format(self.focus.latex(),
                                                       self.structuralChange.latex() if self.copyOffset == 0 else self.copyOffset,
                                                       self.leftTriggers.latex(),
                                                       self.rightTriggers.latex())

    
    def mutate(self,bank):
        f = self.focus
        s = self.structuralChange
        l = self.leftTriggers
        r = self.rightTriggers
        if random() < 0.3:
            f = f.mutate(bank) if random() < 0.8 else Specification.sample(bank,
                                                                           s.skeleton() == 'K')
        if random() < 0.3:
            s = s.mutate(bank) if random() < 0.8 else Specification.sample(bank, f.skeleton() != '0')
        if random() < 0.3:
            l = l.mutate(bank) if random() < 0.8 else Guard.sample(bank,'L')
        if random() < 0.3:
            r = r.mutate(bank) if random() < 0.8 else Guard.sample(bank,'R')
        return Rule(f,s,l,r,0)

    def calculateMapping(self,bank):
        insertion = False
        deletion = isinstance(self.structuralChange,EmptySpecification)
        
        # construct the input/output mapping
        if isinstance(self.focus,ConstantPhoneme):
            inputs = [self.focus.p]
        elif isinstance(self.focus,FeatureMatrix):
            inputs = [ p
                       for p in bank.phonemes
                       if self.focus.matches(featureMap[p]) ]
        elif isinstance(self.focus,EmptySpecification):
            # insertion rule
            assert isinstance(self.structuralChange,ConstantPhoneme)
            insertion = True
            inputs = ['']
        else: assert False

        if deletion:
            outputs = [ '' for _ in inputs ]
        else:
            if not insertion:
                outputs = [ frozenset(self.structuralChange.apply(featureMap[i])) for i in inputs ]
            else:
                outputs = [ frozenset(featureMap[self.structuralChange.p]) ]
            if getVerbosity() >= 5: print "outputs = ",outputs
            outputs = [ bank.matrix2phoneme.get(o,None) for o in outputs ]

        return dict([ (i,o) for (i,o) in zip(inputs, outputs) ])

    def fst(self,bank):
        if unicode(self) in Rule.SAVEDTRANSDUCERS: return Rule.SAVEDTRANSDUCERS[unicode(self)]

        insertion = False
        deletion = isinstance(self.structuralChange,EmptySpecification)
        
        mapping = self.calculateMapping(bank)
        if getVerbosity() >= 5:
            print "MAPPING"
            print self
            print "\n".join([ u'\t%s > %s\n'%(x,y) for (x,y) in mapping.iteritems() ])
            print

        if len(mapping) == 0: raise InvalidRule('mapping has length zero')

        mapping = dict([ (i if insertion else bank.phoneme2fst(i),
                          # '.' is magical error signal
                          o if deletion  else ('.' if o == None else bank.phoneme2fst(o)))
                         for i,o in mapping.iteritems() ])
        if getVerbosity() >= 5:
            print "mapping:"
            print mapping
            print
        regex = transducerOfRule(mapping,
                                 self.leftTriggers.fst(bank),
                                 self.rightTriggers.fst(bank),
                                 bank.transducerAlphabet())
        
        Rule.SAVEDTRANSDUCERS[unicode(self)] = regex
        return regex        

    # Produces sketch object
    def makeConstant(self, bank):
        return Constant("new Rule(focus = %s, structural_change = %s, left_trigger = %s, right_trigger = %s, copyOffset = %d)" % (self.focus.makeConstant(bank),
                                                                                                                                  self.structuralChange.makeConstant(bank),
                                                                                                                                  self.leftTriggers.makeConstant(bank),
                                                                                                                                  self.rightTriggers.makeConstant(bank),
                                                                                                                                  self.copyOffset))

    # Returns a variable that refers to a sketch object
    def makeDefinition(self, bank):
        return define("Rule", self.makeConstant(bank))
                                         
    # Produces sketch object
    @staticmethod
    def sample():
        return define("Rule", FunctionCall("unknown_rule",[]))

    # Produces a rule object from a sketch output
    @staticmethod
    def parse(bank, output, variable):
        pattern = 'Rule.*%s.* = new Rule\(focus=([a-zA-Z0-9_]+), structural_change=([a-zA-Z0-9_]+), left_trigger=([a-zA-Z0-9_]+), right_trigger=([a-zA-Z0-9_]+), copyOffset=([0-9\-\(\)]+)\)' % str(variable)
        m = re.search(pattern, output)
        if not m:
            raise Exception('Failure parsing rule')
        focus = Specification.parse(bank, output, m.group(1))
        structuralChange = Specification.parse(bank, output, m.group(2))
        leftTrigger = Guard.parse(bank, output, m.group(3), 'L')
        rightTrigger = Guard.parse(bank, output, m.group(4), 'R')
        copyOffset = int("".join([ c for c in m.group(5) if not c in [')','('] ]))
        return Rule(focus, structuralChange, leftTrigger, rightTrigger, copyOffset)

    def apply(self, u):
        # First off we convert u to feature matrices if it is a morph
        if isinstance(u,Morph):
            u = [ featureMap[p] for p in u.phonemes ]
            
        middleOkay = [ self.focus.matches(p) for p in u ]

        leftOkay = []
        accepting = False
        # check to see if the left matches
        for j in range(len(u)):
            okay = True
            if self.leftTriggers.starred:
                if j == 0:
                    okay = False
                    accepting = self.leftTriggers.specifications[1].matches(u[0])
                else:
                    okay = accepting
                    accepting = ((not self.leftTriggers.endOfString) and self.leftTriggers.specifications[1].matches(u[j])) or (accepting and self.leftTriggers.specifications[0].matches(u[j]))
            elif self.leftTriggers.endOfString and len(self.leftTriggers.specifications) == 0: # #_
                okay = j == 0
            elif self.leftTriggers.specifications != []:
                okay = j > 0 and self.leftTriggers.specifications[0].matches(u[j - 1])
                if len(self.leftTriggers.specifications) == 2: # (#?)gg_
                    okay = okay and j > 1 and self.leftTriggers.specifications[1].matches(u[j - 2])

                if self.leftTriggers.endOfString:
                    if len(self.leftTriggers.specifications) == 1:
                        okay = okay and j == 1
                    else:
                        okay = okay and j == 2
            leftOkay.append(okay)

        # do the same thing on the right but walk backwards
        rightOkay = [None]*len(u)
        accepting = False
        for j in range(len(u) - 1, -1, -1):
            okay = True
            if self.rightTriggers.starred: # _g*g(#?)
                if j == len(u) - 1:
                    okay = False
                    accepting = self.rightTriggers.specifications[1].matches(u[len(u) - 1])
                else:
                    okay = accepting
                    accepting = ((not self.rightTriggers.endOfString) and self.rightTriggers.specifications[1].matches(u[j])) or (accepting and self.rightTriggers.specifications[0].matches(u[j]))
            elif self.rightTriggers.endOfString and self.rightTriggers.specifications == []: # _#
                okay = j == len(u) - 1
            elif self.rightTriggers.specifications != []: # _gg?#?
                okay = j < len(u) - 1 and self.rightTriggers.specifications[0].matches(u[j + 1])
                if len(self.rightTriggers.specifications) == 2: # _gg#?
                    okay = okay and j < len(u) - 2 and self.rightTriggers.specifications[1].matches(u[j + 2])

                if self.rightTriggers.endOfString:
                    if len(self.rightTriggers.specifications) == 1: # _g#
                        okay = okay and j == len(u) - 2
                    else: # _gg#
                        okay = okay and j == len(u) - 3
            rightOkay[j] = okay
                
            
        triggered = [ middleOkay[j] and rightOkay[j] and leftOkay[j] for j in range(len(u)) ]

        change = self.structuralChange
        if isinstance(change,EmptySpecification):
            return [ u[j] for j in range(len(u)) if not triggered[j] ]
        elif isinstance(self.focus, EmptySpecification):
            output = []
            if self.rightTriggers.endOfString and self.rightTriggers.specifications == []: # l_#
                pass
            for j in range(len(u)):
                if j > 0 and leftOkay[j] and rightOkay[j - 1]:
                    output.append(change.apply(None))
                output.append(u[j])
            return output
        else:
            return [ (u[j] if not triggered[j] else change.apply(u[j])) for j in range(len(u)) ]


    @staticmethod
    def enumeration(b,cost):
        def enumerateFocus():
            focuses = Specification.enumeration(b,cost)
            if cost > 1: focuses += [EmptySpecification()]
            return focuses
        def enumerateChange(focus):
            fc = focus.cost()
            isInsertion = isinstance(focus,EmptySpecification)
            if not isInsertion:
                changes = Specification.enumeration(b,cost - fc)
                if cost - fc > 1: changes += [EmptySpecification()]
            else:
                changes = ConstantPhoneme.enumeration(b,cost - fc)
            return changes
        results = []
        for focus in enumerateFocus():
            for change in enumerateChange(focus):
                c1 = cost - focus.cost() - change.cost()
                for gl in Guard.enumeration('L',b,c1):
                    for gr in Guard.enumeration('R',b,c1 - gl.cost()):
                        results.append(Rule(focus,change,gl,gr,0))
        return results


EMPTYRULE = Rule(focus = FeatureMatrix([]),
                 structuralChange = FeatureMatrix([]),
                 leftTriggers = Guard('L',False,False,[]),
                 rightTriggers = Guard('R',False,False,[]),
                 copyOffset = 0)
assert EMPTYRULE.doesNothing()

if __name__ == '__main__':
    from problems import *
    b = FeatureBank([w
                     for l in interactingProblems[4].data for w in l ])
    for c in range(9):
        print "# rules of cost less than",c,"is",len(Rule.enumeration(b,c))

