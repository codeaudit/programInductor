# -*- coding: utf-8 -*-

from parseSPE import parseRule
from rule import *
from time import time
from math import log
from utilities import *

from os import system
import cProfile
from multiprocessing import Pool

class MatchFailure(Exception):
    pass

class Fragment():
    def __str__(self): return unicode(self).encode('utf-8')
    def __eq__(self,other): return unicode(self) == unicode(other)
    def __hash__(self):
        return hash(str(self))
    def match(self,program): raise Exception('Match not implemented for fragment: %s'%str(self))

class VariableFragment(Fragment):
    def __init__(self, ty):
        # ty should be a Python class within the rule structure
        # for example it could be Rule, FeatureMatrix, ...
        self.ty = ty
        self.logPrior = -1.6
    def __unicode__(self): return unicode(self.ty.__name__)
    def match(self, program):
        if isinstance(program,self.ty):
            return [(self.ty,program)]
        raise MatchFailure()
    def sketchCost(self,v,b):
        calculator = {}
        calculator[FC] = 'specification_cost'
        calculator[Guard] = 'guard_cost'
        calculator[FeatureMatrix] = 'specification_cost'
        calculator[ConstantPhoneme] = 'specification_cost'
        return ([], '%s(%s)'%(calculator[self.ty],v))

class RuleFragment(Fragment):
    CONSTRUCTOR = Rule
    def __init__(self, focus, change, left, right):
        self.focus, self.change, self.left, self.right = focus, change, left, right
        self.logPrior = focus.logPrior + change.logPrior + left.logPrior + right.logPrior
    def match(self,program):
        return self.focus.match(program.focus) + self.change.match(program.structuralChange) + self.left.match(program.leftTriggers) + self.right.match(program.rightTriggers)
    def __unicode__(self):
        return u"{} ---> {} / {} _ {}".format(self.focus,
                                              self.change,
                                              self.left,
                                              self.right)
    @staticmethod
    def abstract(p,q):
        if p.copyOffset != 0 or q.copyOffset != 0:
            raise Exception('abstractRuleFragments: copy offsets not yet supported')

        return [
            RuleFragment(focus,change,l,r)
            for focus in FCFragment.abstract(p.focus,q.focus)
            for change in FCFragment.abstract(p.structuralChange,q.structuralChange)
            for l in GuardFragment.abstract(p.leftTriggers, q.leftTriggers)
            for r in GuardFragment.abstract(p.rightTriggers,q.rightTriggers)
        ]

    def sketchCost(self,v,b):
        '''v: string representation of a sketch variable. v should have type Rule in the actual sketch.
        b: a feature bank
        returns: (listOfChecksThatHavetoBeTrueToMatch, listOfExtraExpenses)'''
        (fc,fe) = self.focus.sketchCost('%s.focus'%v,b)
        (sc,se) = self.structuralChange.sketchCost('%s.structural_change'%v,b)
        (lc,le) = self.left.sketchCost('%s.left_trigger'%v,b)
        (rc,re) = self.right.sketchCost('%s.right_trigger'%v,b)
        return (fc + sc + rc + lc,
                fe + se + le + re)

    # if isinstance(VariableFragment,self.focus):
    #         # focus is an additional expense
    #         additionalExpenses.append('specification_cost(%s.focus)'%v)
    #     else:
    #         if isinstance(self.focus,MatrixFragment) or isinstance(self.focus.child,EmptySpecification):
    #             checks.append(self.focus.child.sketchEquals('%s.focus'%v,b))
    #         else: assert False
    #     if isinstance(VariableFragment,self.structuralChange):
    #         # focus is an additional expense
    #         additionalExpenses.append('specification_cost(%s.structural_change)'%v)
    #     else:
    #         if isinstance(self.structuralChange,MatrixFragment) or isinstance(self.structuralChange.child,EmptySpecification):
    #             checks.append(self.structuralChange.child.sketchEquals('%s.structural_change'%v,b))
    #         else: assert False
        
RuleFragment.BASEPRODUCTIONS = [RuleFragment(VariableFragment(FC),VariableFragment(FC),
                                             VariableFragment(Guard),VariableFragment(Guard))]

class FCFragment(Fragment):
    CONSTRUCTOR = FC
    def __init__(self, child, logPrior = None):
        self.child = child
        self.logPrior = child.logPrior if logPrior == None else logPrior

    def __unicode__(self): return unicode(self.child)

    def match(self, program):
        if isinstance(program, EmptySpecification):
            if isinstance(self.child, EmptySpecification):
                return []
            else:
                raise MatchFailure()
        else:
            if isinstance(self.child, EmptySpecification):
                raise MatchFailure()
            else:
                return self.child.match(program)
    def sketchCost(self,v,b):
        assert isinstance(self.child,EmptySpecification)
        return (['(%s == null)'%v],[])

    @staticmethod
    def abstract(p,q):
        fragments = []
        if unicode(p) != unicode(q):
            fragments += [VariableFragment(FC)]
        # if isinstance(p,EmptySpecification) and isinstance(q,EmptySpecification):
        #     fragments += [FCFragment(EmptySpecification(), -1)]
        if (not isinstance(p,EmptySpecification)) and (not isinstance(q,EmptySpecification)):
            fragments += SpecificationFragment.abstract(p,q)
        return fragments

FCFragment.BASEPRODUCTIONS = [FCFragment(EmptySpecification(),-1),
                              FCFragment(VariableFragment(Specification))]

class SpecificationFragment(Fragment):
    CONSTRUCTOR = Specification
    def __init__(self, child, logPrior = None):
        self.child = child
        self.logPrior = child.logPrior if logPrior == None else logPrior

    def __unicode__(self): return unicode(self.child)

    def match(self, program):
        return self.child.match(program)

    @staticmethod
    def abstract(p,q):
        fragments = []
        if unicode(p) != unicode(q):
            fragments += [VariableFragment(FeatureMatrix)]
        if isinstance(p,FeatureMatrix) and isinstance(q,FeatureMatrix):
            fragments += MatrixFragment.abstract(p,q)
        if isinstance(p,ConstantPhoneme) and isinstance(q,ConstantPhoneme):
            fragments += ConstantFragment.abstract(p,q)
        return fragments

    def sketchCost(self,v,b):
        assert False
SpecificationFragment.BASEPRODUCTIONS = [SpecificationFragment(VariableFragment(FeatureMatrix)),
                                         SpecificationFragment(VariableFragment(ConstantPhoneme))]

class MatrixFragment(Fragment):
    CONSTRUCTOR = FeatureMatrix
    def __init__(self, child, logPrior = None):
        self.child = child
        self.childUnicode = unicode(child)
        self.logPrior = None#child.logPrior if logPrior == None else logPrior

    def __unicode__(self): return self.childUnicode

    def match(self, program):
        if unicode(program) == self.childUnicode: return []
        raise MatchFailure()
        
    @staticmethod
    def abstract(p,q):
        if unicode(p) == unicode(q):
            if len(p.featuresAndPolarities) < 3:
                return [MatrixFragment(p, emptyFragmentGrammar.matrixLogLikelihood(p))]
            else:
                return [] # prefer matrix fragments that are short
        else:
            return [VariableFragment(FeatureMatrix)]

    def sketchCost(self,v,b):
        assert isinstance(self.child,FeatureMatrix)
        return ([self.child.sketchEquals(v,b)],[])

MatrixFragment.BASEPRODUCTIONS = [] #VariableFragment(FeatureMatrix)]

class ConstantFragment(Fragment):
    CONSTRUCTOR = ConstantPhoneme
    def __init__(self): raise Exception('should never make a constant fragment')
    def __unicode__(self): raise Exception('should never try to print the constant fragment')
    @staticmethod
    def abstract(p,q):
        return [VariableFragment(ConstantPhoneme)]
ConstantFragment.BASEPRODUCTIONS = [] #VariableFragment(ConstantPhoneme)]

class GuardFragment(Fragment):
    CONSTRUCTOR = Guard
    def __init__(self, specifications, endOfString, starred):
        self.logPrior = sum([s.logPrior for s in specifications ])
        if starred: self.logPrior -= 1.0
        if endOfString: self.logPrior -= 1.0

        self.specifications = specifications
        self.starred = starred
        self.endOfString = endOfString

    def __unicode__(self):
        parts = map(unicode, self.specifications)
        if self.starred: parts[-2] += u'*'
        if self.endOfString: parts += [u'#']
        return u" ".join(parts)

    def match(self, program):
        if self.endOfString != program.endOfString or self.starred != program.starred or len(self.specifications) != len(program.specifications):
            raise MatchFailure()

        return [ binding for f,p in zip(self.specifications,program.specifications)
                 for binding in f.match(p) ]

    @staticmethod
    def abstract(p,q):
        if p.endOfString != q.endOfString or p.starred != q.starred or len(p.specifications) != len(q.specifications):
            return [VariableFragment(Guard)]
        if len(p.specifications) == 0:
            return [GuardFragment([],p.endOfString,False)]
        if len(p.specifications) == 1:
            return [GuardFragment([s1],p.endOfString,p.starred)
                    for s1 in SpecificationFragment.abstract(p.specifications[0],q.specifications[0]) ]
        if len(p.specifications) == 2:
            return [GuardFragment([s1,s2],p.endOfString,p.starred)
                    for s1 in SpecificationFragment.abstract(p.specifications[0],q.specifications[0])
                    for s2 in SpecificationFragment.abstract(p.specifications[1],q.specifications[1])]
        raise Exception('GuardFragment.abstract: should never reach this point')

    def sketchCost(self,v,b):
        checks = ['(%s.endOfString = %d)'%(v,int(self.endOfString)),
                  '(%s.starred = %d)'%(v,int(self.starred))]
        expenses = []
        for component, suffix in zip(self.specifications,['spec','spec2']):
            k,e = component.sketchCost('%s.%s'%(v,suffix),b)
            checks += k
            expenses += e
        return (checks, expenses)
GuardFragment.BASEPRODUCTIONS = [GuardFragment([VariableFragment(Specification)]*s,e,starred)
                                 for e in [True,False]
                                 for s in range(3)
                                 for starred in ([True,False] if s > 1 else [False]) ]    

def programSubexpressions(program):
    '''Yields the sequence of tuples of (ty,expression)'''
    if isinstance(program, Rule):
        yield (Rule,program)
        for x in programSubexpressions(program.focus): yield x
        for x in programSubexpressions(program.structuralChange): yield x
        for x in programSubexpressions(program.leftTriggers): yield x
        for x in programSubexpressions(program.rightTriggers): yield x
    elif isinstance(program, Guard):
        yield (Guard, program)
        for x in programSubexpressions(program.specifications): yield x
    elif isinstance(program, FeatureMatrix):
        yield (Specification, program)
       
    
def proposeFragments(problems, verbose = False):
    ruleSets = []
    for problem in problems:
        # problem should be a list of solutions
        # each solution should be a list of rules
        ruleSets.append(set([ r for s in problem for r in s ]))

    abstractFragments = {
        Rule: RuleFragment.abstract,
        Guard: GuardFragment.abstract,
        Specification: SpecificationFragment.abstract
    }

    # Don't allow fragments that are already in the grammar, for example SPECIFICATION -> MATRIX
    badFragments = {
        Guard: [Guard],
        Specification: [FeatureMatrix,ConstantPhoneme,Specification,'[  ]'],
        Rule: [Rule]
        }

    startTime = time()
    fragments = {} # map from type to a set of fragments
    for i in range(len(ruleSets) - 1):
        for j in range(i+1, len(ruleSets)):
            for p in ruleSets[i]:
                for q in ruleSets[j]:
                    for pt,pf in programSubexpressions(p):
                        fragments[pt] = fragments.get(pt,set([]))
                        for qt,qf in programSubexpressions(q):
                            if pt != qt: continue

                            # the extra condition here is to avoid fragments like "GUARD -> GUARD"
                            newFragments = [ f for f in abstractFragments[pt](pf,qf)
                                             if not (str(f) in badFragments[pt]) ]
                            # if [ f for f in newFragments if "instance at" in str(f) ]:
                            #     print pt,pf
                            #     print qt,qf
                            #     print [ str(f) for f in newFragments if "instance at" in str(f) ]
                            #     assert False
                            fragments[pt] = fragments[pt] | set(newFragments)


    totalNumberOfFragments = sum([len(v) for v in fragments.values() ])
    print "Discovered %d unique fragments in %f seconds"%(totalNumberOfFragments,time() - startTime)
    if verbose:
        for ty in fragments:
            print "Fragments of type %s (%d):"%(ty,len(fragments[ty]))
            for f in fragments[ty]:
                print f
            print ""

    return [ (t, f) for t in fragments for f in fragments[t] ] # if t != Rule ] #and t != 'GUARD' ]

def fragmentLikelihood(parameters):
    (problems, fragments, newFragment) = parameters
    newGrammar = FragmentGrammar(fragments + [newFragment])
    l = sum([ max([ sum([ newGrammar.ruleLogLikelihood(r) for r in s ]) for s in problem ])
              for problem in problems ])
    posterior = l + newFragment[1].logPrior
    f = newFragment
    print "Considering %s %s\n\t%f + %f = %f"%(f[0],f[1],l,f[1].logPrior,posterior)
    return (f, l)
    
def pickFragments(problems, fragments, maximumGrammarSize):
    chosenFragments = []

    expressionTable = {}
    problems = [ [ [ r.share(expressionTable) for r in s ] for s in p ]
                 for p in problems ]

    oldPosterior = None

    def showMostLikelySolutions():
        g = FragmentGrammar(chosenFragments)
        for j,p in enumerate(problems):
            bestLikelihood,bestSolution = max([ (sum([ g.ruleLogLikelihood(r) for r in s ]), s)
                                                for s in p ])
            print "Problem %d"%j
            for r in bestSolution:print "\t%s"%(str(r))
            print

    showMostLikelySolutions()

    typeOrdering = [Specification,Guard,Rule]

    startTime = time()
    while len(chosenFragments) < maximumGrammarSize:
        candidateFragments = [ x for x in fragments if not x in chosenFragments and x[0] == typeOrdering[0] ]
        parameters = [ (problems, chosenFragments, x) for x in candidateFragments ]
        fragmentLikelihoods = map(fragmentLikelihood, parameters)

        # What is the best fragment according to the likelihood, breaking ties by the prior?
        priorWeight = 0.75
        ((bestType,bestFragment),bestLikelihood) = max(fragmentLikelihoods, key = lambda (f,l): (l+priorWeight*f[1].logPrior))
        print "The best fragment as measured by adjusted posterior is:"
        bestPrior = bestFragment.logPrior
        bestPosterior = bestPrior+bestLikelihood
        print bestType,bestFragment,bestLikelihood,"+",bestPrior,"=",bestPosterior
        
        # but is it good enough to keep?
        newPosterior = bestLikelihood # + sum([ f[1].logPrior for f in chosenFragments ]) + bestPrior
        if oldPosterior != None and newPosterior < oldPosterior:
            print "But, adding nothing is better than adding that fragment."
            if typeOrdering == []:
                break
            else:
                typeOrdering = typeOrdering[1:]
                print "Moving onto fragments of type %s"%typeOrdering[0]
                continue
        
        oldPosterior = newPosterior
        print "New posterior w/ all priors accounted for:",newPosterior            
        chosenFragments.append((bestType,bestFragment))
        showMostLikelySolutions()
    print "Final grammar:"
    for t,f in chosenFragments: print t,f
    print "Search time:",(time() - startTime),"seconds"
    return chosenFragments

def induceGrammar(problems, maximumGrammarSize = 20):
    fragments = proposeFragments(problems, verbose = True)
    p = problems
    picker = pickFragments
    chosenFragments = picker(p, fragments, maximumGrammarSize)

    return FragmentGrammar(chosenFragments)
            

class FragmentGrammar():
    def __init__(self, fragments = []):
        self.featureLogLikelihoods = {}

        # memorization table for likelihood calculations
        self.ruleTable = {}
        self.guardTable = {}
        self.matrixTable = {}
        self.specificationTable = {}
        self.fCTable = {}
        
        self.likelihoodCalculator = {}
        self.likelihoodCalculator[Rule] = lambda r: self.ruleLogLikelihood(r)
        self.likelihoodCalculator[Specification] = lambda s: self.specificationLogLikelihood(s)
        self.likelihoodCalculator[Guard] = lambda g: self.guardLogLikelihood(g)
        self.likelihoodCalculator[ConstantPhoneme] = lambda k: self.constantLogLikelihood(k)
        self.likelihoodCalculator[FeatureMatrix] = lambda m: self.matrixLogLikelihood(m)
        self.likelihoodCalculator[FC] = lambda fc:  self.fCLogLikelihood(fc)
        
        # different types of fragments
        # fragments of type rule, etc
        self.ruleFragments = normalizeLogDistribution([ (l,f) for t,l,f in fragments if t == Rule ])
        self.guardFragments = normalizeLogDistribution([ (l,f) for t,l,f in fragments if t == Guard ])
        self.specificationFragments = normalizeLogDistribution([ (l,f) for t,l,f in fragments if t == Specification ])
        self.fragments = fragments

        self.numberOfPhonemes = 40 # should this be the number of phonemes? or number of phonemes in a data set?
        self.numberOfFeatures = 40 # same thing

    def __str__(self):
        return formatTable([ ["%01f"%l,"%s ::="%t.__name__, str(f) ]
                             for t,l,f in self.fragments])

    def fragmentLikelihood(self, program, fragments):
        ll = float('-inf')
        for lf,fragment in fragments:
            try:
                m = fragment.match(program)
            except MatchFailure:
                continue
            
            fragmentLikelihood = 0.0
            for childType,child in m:
                fragmentLikelihood += self.likelihoodCalculator[childType](child)
            ll = lse(ll, fragmentLikelihood + lf)
        return ll
        
    def ruleLogLikelihood(self, r):
        key = unicode(r)
        if key in self.ruleTable:
            return self.ruleTable[key]
        
        ll = self.fragmentLikelihood(r, self.ruleFragments)
        self.ruleTable[key] = ll
        return ll

    def fCLogLikelihood(self,s):
        key = unicode(s)
        if key in self.fCTable: return self.fCTable[key]
        ll = self.fragmentLikelihood(s, self.specificationFragments)
        self.fCTable[key] = ll
        return ll
    
    def specificationLogLikelihood(self, s):
        key = unicode(s)
        if key in self.specificationTable: return self.specificationTable[key]
        ll = self.fragmentLikelihood(s, self.specificationFragments)
        self.specificationTable[key] = ll
        return ll

    def constantLogLikelihood(self, k):
        if isinstance(k,ConstantPhoneme):
            return -log(float(self.numberOfPhonemes))
        else:
            raise Exception('constantLogLikelihood: did not get a constant')

    def matrixSizeLogLikelihood(self,l):
        if l == 0: return log(0.3)
        if l == 1: return log(0.6)
        return log(0.05)

    def matrixLogLikelihood(self, m):
        if isinstance(m,FeatureMatrix):
            # empirical probabilities on matrix problems: [(0, 0.3225806451612903), (1, 0.6129032258064516), (2, 0.03225806451612903), (3, 0.03225806451612903)]
            return len(m.featuresAndPolarities)*(-log(float(self.numberOfFeatures))) + self.matrixSizeLogLikelihood(len(m.featuresAndPolarities))
        else:
            raise Exception('matrixLogLikelihood')

    def guardLengthLogLikelihood(self,l):
        if l == 0: return log(0.5)
        if l == 1: return log(0.33)
        if l == 2: return log(0.17)
        raise Exception('unhandled guardflength')

    def guardLogLikelihood(self, m):
        key = unicode(m)
        if key in self.guardTable: return self.guardTable[key]
        ll = self.fragmentLikelihood(m, self.guardFragments)
        self.guardTable[key] = ll
        return ll

    def sketchUniversalGrammar(self,bank):
        from sketchSyntax import definePreprocessor
        definitions = {}
        for dictionaryKey, fragments, v in [('UNIVERSALRULEGRAMMAR',self.ruleFragments,'r'),
                                            ('UNIVERSALSPECIFICATIONGRAMMAR',self.specificationFragments,'s'),
                                            ('UNIVERSALGUARDGRAMMAR',self.guardFragments, 'g')]:
            for checks, expenses in sorted([ r.sketchCost(v,bank) for r in fragments],
                                           key = lambda z: len(z[1])):
                check = "&&".join(['1'] + checks)
                cost = " + ".join(['1'] + expenses)
                definitions[dictionaryKey] = definitions.get(dictionaryKey,'')
                definitions[dictionaryKey] += " if (%s) return %s; "%(check, cost)
        for k,v in definitions.iteritems():
            definePreprocessor(k,v)

        
BASEPRODUCTIONS = [(k.CONSTRUCTOR, 0, f)
                   for k in [RuleFragment,FCFragment,SpecificationFragment,MatrixFragment,ConstantFragment,GuardFragment]
                   for f in k.BASEPRODUCTIONS]
BASEPRODUCTIONS += [(Specification, 0, MatrixFragment(FeatureMatrix([(False,'voice')])))]
emptyFragmentGrammar = FragmentGrammar(BASEPRODUCTIONS)
print str(emptyFragmentGrammar)
r = parseRule('e > a / # _ [ -voice ]* h #')
print r
print emptyFragmentGrammar.ruleLogLikelihood(r)
# manualFragmentGrammar = FragmentGrammar([(Rule,
#                                           RuleFragment(MatrixFragment()))])

def pseudoCountPenalty(pc, fragments):
    if len(fragments) == 0:
        return 0.0,float('-inf')
    return log(float(pc)/(len(fragments)+pc)),log(float(len(fragments))/(len(fragments)+pc))
