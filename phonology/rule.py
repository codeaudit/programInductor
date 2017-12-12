# -*- coding: utf-8 -*-

from problems import interactingProblems
from sketchSyntax import define, FunctionCall, Constant, Variable, getGeneratorDefinition, globalConstant
from features import FeatureBank,featureMap,tokenize
from latex import latexWord
from morph import Morph
from utilities import *


import re
from random import choice,random
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

# abstract class for focus/change
class FC():
    def __init__(self): pass

class Specification():
    def __init__(self): pass

    @staticmethod
    def sample(bank, canBeEmpty = False):
        import numpy as np
        
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
        parsers = [FeatureMatrix.parse,EmptySpecification.parse,ConstantPhoneme.parse,BoundarySpecification.parse]
        for parser in parsers:
            try:
                return parser(bank, output, variable)
            except:
                continue
        assert False,"Parse failure for specification"

    @staticmethod
    def enumeration(b,cost):
        return ConstantPhoneme.enumeration(b,cost) + FeatureMatrix.enumeration(b,cost)
        
class ConstantPhoneme(Specification,FC):
    def __init__(self, p): self.p = p
    def __unicode__(self):
        if self.p == '-': return u"σ"
        else: return self.p
    def __str__(self): return unicode(self).encode('utf-8')
    def doesNothing(self): return False
    def cost(self): return 2
    def skeleton(self): return "K"
    def latex(self): return latexWord(self.p)
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

    def sketchEquals(self,v,b):
        return "(extract_constant_sound(%s) == phoneme_%d)"%(v,b.phoneme2index[self.p])

class EmptySpecification(FC):
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

    def sketchEquals(self,v,_):
        return "((%s) == null)"%(v)

class OffsetSpecification(FC):
    def __init__(self,offset):
        assert offset != 0
        self.offset = offset
    def __unicode__(self): return unicode(self.offset)
    def __str__(self): return unicode(self).encode('utf-8')

    def doesNothing(self): return False
    def skeleton(self): return "Z"
    def cost(self): return 1
    def latex(self): return '$%d$'%self.offset
    def mutate(self,_): return self

    def share(self, table):
        k = ('OFFSETSPECIFICATION',unicode(self))
        if k in table: return table[k]
        table[k] = self
        return self

    def merge(self, other):
        if isinstance(other, OffsetSpecification) and self.offset == other.offset: return self
        return Braces(self, other)

    @staticmethod
    def parse(bank, output, variable):
        print "Fatal error: attempt to parse OffsetSpecification"
        assert False
    def makeConstant(self, bank):
        return FeatureMatrix([]).makeConstant(bank)

    def matches(self, test):
        raise Exception('cannot match offset')
    def apply(self, test):
        raise Exception('cannot apply offset')

    def sketchEquals(self,v,bank):
        return FeatureMatrix([]).sketchEquals(v,bank)

class BoundarySpecification(Specification):
    def __init__(self): pass
    def __unicode__(self): return u"+"
    def __str__(self): return unicode(self).encode('utf-8')

    def doesNothing(self): return False
    def skeleton(self): return "+"
    def cost(self): return 2
    def latex(self): return '$+$'
    def mutate(self,_): return self
    def extension(self,_): return "+"

    def share(self, table):
        k = ('BOUNDARYSPECIFICATION',unicode(self))
        if k in table: return table[k]
        table[k] = self
        return self

    def merge(self, other):
        if isinstance(other, BoundarySpecification): return self
        return Braces(self, other)

    @staticmethod
    def parse(bank, output, variable):
        if "global_boundary_specification" in variable:
            return BoundarySpecification()
        else:
            raise Exception('Failure parsing boundary specification %s'%variable)
    
    def makeConstant(self, bank):
        return "global_boundary_specification"

    def matches(self, test):
        return False
    def apply(self, test):
        raise Exception('cannot apply boundary specification')

    def sketchEquals(self,v,_):
        return "(boundary_specification(%s))"%(v)
    
class FeatureMatrix(Specification,FC):
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
        pattern = " %s = new Vector\(([^\)]+)\)"%variable
        m = re.search(pattern, output)
        if not m: raise Exception('Failure parsing Vector %s'%variable)
        try:
            bindings = m.group(1).split(", ")
            bindings = dict( tuple(b.split("=")) for b in bindings)
            return FeatureMatrix([ (bindings[f] == "1",f) for f in bank.features
                                   if bindings[f + "_specified"] == "1"])
        except:
            print "Some kind of fatal parsing problem with feature matrix"
            print output
            print variable
            print m.group(1)
            assert False

    def makeConstant(self, bank):
        arguments = ", ".join([ "%s = %d, %s_specified = %d"%(f,
                                                              int((True,f) in self.featuresAndPolarities),
                                                              f,
                                                              int((True,f) in self.featuresAndPolarities or (False,f) in self.featuresAndPolarities))
                                for f in bank.features ])
        return "new Vector(%s)"%arguments

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
        if False:
            if cost < 1: return []
            cost -= 1
            results = []
            for k in range(cost + 1):
                for features in itertools.combinations(b.features,k):
                    for polarities in itertools.product(*([(True,False)]*k)):
                        results.append(FeatureMatrix(zip(polarities, features)))
            return results
        else:
            if cost < 1: return []
            cost -= 1
            results = {}
            for k in range(cost + 1):
                for features in itertools.combinations(b.features,k):
                    for polarities in itertools.product(*([(True,False)]*k)):
                        matrix = FeatureMatrix(zip(polarities, features))
                        extension = frozenset(matrix.extension(b))
                        if not (extension in results):
                            results[extension] = matrix
            return results.values()

    def sketchEquals(self,v,b):
        return "specification_equal(%s, %s)"%(v,self.makeConstant(b))

class Guard():
    def __init__(self, side, endOfString, optionalEnding, starred, specifications):
        self.side = side
        self.endOfString = endOfString
        self.optionalEnding = optionalEnding
        assert not (optionalEnding and endOfString)
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
        return int(self.starred) + int(self.endOfString) + sum([ s.cost() for s in self.specifications ]) + 2*int(self.optionalEnding)
    
    def __str__(self): return unicode(self).encode('utf-8')
    def __unicode__(self):
        if not hasattr(self, 'representation') or self.representation == None:
            parts = []
            parts += map(unicode,self.specifications)
            if self.starred: parts[-2] += u'*'
            if self.endOfString: parts += [u'#']
            if self.optionalEnding: parts[-1] = u"{#,%s}"%parts[-1]
            if self.side == 'L': parts.reverse()
            self.representation = u" ".join(parts)
        return self.representation
    def pretty(self, copyOffset):
        parts = []
        parts += map(unicode,self.specifications)
        if self.starred: parts[-2] += u'*'
        if self.optionalEnding: parts[-1] = u"{#,%s}"%parts[-1]
        if copyOffset != 0:
            if copyOffset < 0 and self.side == 'L': parts[-copyOffset - 1] += u'ᵢ'
            if copyOffset > 0 and self.side == 'R': parts[copyOffset - 1] += u'ᵢ'
        if self.endOfString: parts += [u'#']
        if self.side == 'L': parts.reverse()
        return u" ".join(parts)

    def groundAdjacent(self,p):
        assert self.side == 'R'
        assert not self.starred
        newSpecifications = list(self.specifications)
        newSpecifications[0] = ConstantPhoneme(p)
        return Guard('R', self.endOfString, False, newSpecifications)
        
    
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
        if self.endOfString: parts += ['\\#']
        if self.optionalEnding: parts[-1] = "\\{%s,\\#\\}"%(parts[-1])
        if self.side == 'L': parts.reverse()
        return " ".join(parts)

    
    def share(self, table):
        k = ('GUARD',self.side,unicode(self))
        if k in table: return table[k]
        table[k] = Guard(self.side, self.endOfString, self.optionalEnding, self.starred,
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
        pattern = " %s = new Guard\(endOfString=([01]), optionalEndOfString=([01]), starred=([01]), spec=([a-zA-Z0-9_]+), spec2=([a-zA-Z0-9_]+)"%variable
        m = re.search(pattern, output)
        if not m: raise Exception('Could not parse guard %s using pattern %s'%(variable,pattern))

        endOfString = m.group(1) == '1'
        optionalEnding = m.group(2) == '1'
        starred = m.group(3) == '1'
        spec = None if m.group(4) == 'null' else Specification.parse(bank, output, m.group(4))
        if isinstance(spec,EmptySpecification): spec = None
        spec2 = None if m.group(5) == 'null' else Specification.parse(bank, output, m.group(5))
        if isinstance(spec2,EmptySpecification): spec2 = None
        return Guard(side, endOfString, optionalEnding, starred, [spec,spec2])
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
        
        return "new Guard(endOfString = %d, optionalEndOfString = %d, starred = %d, spec = %s, spec2 = %s)" % (1 if self.endOfString else 0,
                                                                                                               1 if self.optionalEnding else 0,
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

    def sketchEquals(self,v,b):
        if len(self.specifications) > 0:
            spec1 = self.specifications[0].sketchEquals(v + '.spec',b)
        else: spec1 = '%s.spec == null'%v
        if len(self.specifications) > 1:
            spec2 = self.specifications[1].sketchEquals(v + '.spec',b)
        else: spec2 = '%s.spec2 == null'%v
        
        return "(%s.endOfString == %d && %s.optionalEndOfString == %d && %s.starred == %d && %s && %s)"%(v,int(self.endOfString),
                                                                                                         v,int(self.optionalEnding),
                                                                   v,int(self.starred),
                                                                   spec1,spec2)
        
        
    
class Rule():
    def __init__(self, focus, structuralChange, leftTriggers, rightTriggers):
        self.focus = focus
        self.structuralChange = structuralChange
        self.leftTriggers = leftTriggers
        self.rightTriggers = rightTriggers
        self.representation = None # Unicode representation
        if isinstance(self.focus,OffsetSpecification):
            assert isinstance(self.structuralChange,EmptySpecification)
            assert self.focus.offset == 1
        if isinstance(self.structuralChange,OffsetSpecification):
            assert isinstance(self.focus,EmptySpecification)

    def isGeminiRule(self):
        return isinstance(self.focus,OffsetSpecification) and self.focus.offset == 1 and isinstance(self.structuralChange,EmptySpecification)
    def isCopyRule(self):
        return isinstance(self.structuralChange,OffsetSpecification) and isinstance(self.focus,EmptySpecification)

    def merge(self, other):
        return Rule(self.focus.merge(other.focus),
                    self.structuralChange.merge(other.structuralChange),
                    self.leftTriggers.merge(other.leftTriggers),
                    self.rightTriggers.merge(other.rightTriggers))
                    
    def share(self, table):
        k = ('RULE',unicode(self))
        if k in table: return table[k]
        table[k] = Rule(self.focus.share(table),
                        self.structuralChange.share(table),
                        self.leftTriggers.share(table),
                        self.rightTriggers.share(table))
        return table[k]

    def cost(self):
        if self.doesNothing(): return 0
        return self.focus.cost() + self.structuralChange.cost() + self.leftTriggers.cost() + self.rightTriggers.cost()
    def alternationCost(self):
        return self.leftTriggers.cost() + self.rightTriggers.cost()   

    def doesNothing(self):
        '''Does this rule do nothing? Equivalently is it [  ] ---> [  ] /  _ '''
        return self.leftTriggers.doesNothing() and self.rightTriggers.doesNothing() and self.focus.doesNothing() and self.structuralChange.doesNothing()

    def __str__(self): return unicode(self).encode('utf-8')
    def __unicode__(self):
        if not hasattr(self, 'representation') or self.representation == None:
            # check this: should I be calling Unicode recursively?
            self.representation = u"{} ---> {} / {} _ {}".format(unicode(self.focus),
                                                                 unicode(self.structuralChange),
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
                                                       self.structuralChange.latex(),
                                                       self.leftTriggers.latex(),
                                                       self.rightTriggers.latex())

    def pretty(self):
        # deletion & deGemini
        if self.isGeminiRule():
            p = unicode(self.rightTriggers.specifications[0]) + u'ᵢ'
        else:
            p = unicode(self.focus)
        p += u'⟶'
        # insertion and copying
        if self.isCopyRule():
            copyOffset = self.structuralChange.offset
            if copyOffset > 0: p += unicode(self.rightTriggers.specifications[copyOffset - 1])
            else: p += unicode(self.leftTriggers.specifications[-copyOffset - 1])
            p += u'ᵢ'
        else:
            p += unicode(self.structuralChange)
            copyOffset = 0
        p += u' / '
        p += self.leftTriggers.pretty(copyOffset)
        p += u' _ '
        p += self.rightTriggers.pretty(copyOffset)
        p = p.replace(u"[ +vowel ]","V")
        p = p.replace(u"[ -vowel ]","C")
        p = p.replace(u'  ',u" ")
        return p
        
    def calculateCopyOffset(self):
        if isinstance(self.focus,OffsetSpecification): return self.focus.offset
        if isinstance(self.structuralChange,OffsetSpecification): return self.structuralChange.offset
        return 0
    
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
        return Rule(f,s,l,r)

    def calculateMapping(self,bank):
        insertion = False
        deletion = isinstance(self.structuralChange,EmptySpecification)
        
        # construct the input/output mapping
        if isinstance(self.focus,ConstantPhoneme):
            inputs = [self.focus.p]
        elif isinstance(self.focus,FeatureMatrix):
            if not self.isGeminiRule():
                inputs = [ p
                           for p in bank.phonemes
                           if self.focus.matches(featureMap[p]) ]
            else:
                inputs = [p
                          for p in bank.phonemes
                          if self.rightTriggers.specifications[0].matches(featureMap[p]) ]
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

    
    # Produces sketch object
    def makeConstant(self, bank):
        return Constant("new Rule(focus = %s, structural_change = %s, left_trigger = %s, right_trigger = %s, copyOffset = %d)" % (self.focus.makeConstant(bank),
                                                                                                                                  self.structuralChange.makeConstant(bank),
                                                                                                                                  self.leftTriggers.makeConstant(bank),
                                                                                                                                  self.rightTriggers.makeConstant(bank),
                                                                                                                                  self.calculateCopyOffset()))

    # Returns a variable that refers to a sketch object
    def makeDefinition(self, bank):
        return globalConstant("Rule", self.makeConstant(bank))
                                         
    # Produces sketch object
    @staticmethod
    def sample():
        return define("Rule", FunctionCall("unknown_rule",[]), globalToHarnesses = True)

    # Produces a rule object from a sketch output
    @staticmethod
    def parse(bank, output, variable):
        if variable.definingFunction != None:
            # Search for the global definition, get the unique variable name it corresponds to, and parse that
            variable, output = getGeneratorDefinition(variable.definingFunction, output)
            return Rule.parse(bank, output, variable)
        assert isinstance(variable, Variable)
        pattern = 'Rule.*%s.* = new Rule\(focus=([a-zA-Z0-9_]+), structural_change=([a-zA-Z0-9_]+), left_trigger=([a-zA-Z0-9_]+), right_trigger=([a-zA-Z0-9_]+), copyOffset=([0-9\-\(\)]+)\)' % str(variable)
        m = re.search(pattern, output)
        if not m:
            raise Exception('Failure parsing rule')
        focus = Specification.parse(bank, output, m.group(1))
        structuralChange = Specification.parse(bank, output, m.group(2))
        leftTrigger = Guard.parse(bank, output, m.group(3), 'L')
        rightTrigger = Guard.parse(bank, output, m.group(4), 'R')
        copyOffset = int("".join([ c for c in m.group(5) if not c in [')','('] ]))
        if copyOffset != 0:
            if isinstance(focus,EmptySpecification):
                structuralChange = OffsetSpecification(copyOffset)
            elif isinstance(structuralChange,EmptySpecification):
                focus = OffsetSpecification(copyOffset)
            else:
                print "Problem with copy offset in parsed rule:"
                print output
                assert False
        return Rule(focus, structuralChange, leftTrigger, rightTrigger)

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
                changes = [ c for c in Specification.enumeration(b,cost - fc)
                            if not (isinstance(c,FeatureMatrix) and c.featuresAndPolarities == []) and
                            not (isinstance(c,ConstantPhoneme) and isinstance(focus,ConstantPhoneme) and c.p == focus.p)]
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
                        if isinstance(focus,EmptySpecification) and gl.doesNothing() and gr.doesNothing():
                            continue
                        
                        results.append(Rule(focus,change,gl,gr,0))
        return results

    def sketchEquals(self,v,b):
        return "(%s.copyOffset == %d && %s && %s && %s && %s)"%(v,self.calculateCopyOffset(),
                                                                self.focus.sketchEquals(v+'.focus',b),
                                                                self.structuralChange.sketchEquals(v+'.structural_change',b),
                                                                self.leftTriggers.sketchEquals(v+'.left_trigger',b),
                                                                self.rightTriggers.sketchEquals(v+'.right_trigger',b))

    def explain(self,b):
        if self.calculateCopyOffset() == 0:
            print "\tMAPPING:",u"  ".join([ k + u'⟶' + unicode(v)
                                            for k,v in self.calculateMapping(b).iteritems()])
        else:
            print "\tMAPPING: involves copying"
        for s in list(reversed(self.leftTriggers.specifications)) + self.rightTriggers.specifications:
            print "\tspecification_extension:"," ".join(s.extension(b))


EMPTYRULE = Rule(focus = FeatureMatrix([]),
                 structuralChange = FeatureMatrix([]),
                 leftTriggers = Guard('L',False,False,False,[]),
                 rightTriggers = Guard('R',False,False,False,[]))
assert EMPTYRULE.doesNothing()



