
import numpy
from fractions import Fraction,gcd
from functools import reduce

def lcm(a):
    lcM = 1
    n = len(a)
    i = 0
    while i < n:
        a2 = a[i].denominator
        lcM = lcM * a2 / gcd(lcM,a2)
        i += 1
    return int(lcM)
    

def standardize(mat):
    transients = []
    absorbants = []

    for i in range(len(mat)):
        if sum(mat[i]) == 0:
            absorbants.append(i)
        else:
            transients.append(i)
        i += 1
    
    transAbsorbants_R = []
    transTrans_Q = []
    absorbant_I = []

    for i in transients:
        row = []
        for j in absorbants:
            row.append(mat[i][j])
        transAbsorbants_R.append(row)
    
    for i in transients:
        row = []
        for j in transients:
            row.append(mat[i][j])
        transTrans_Q.append(row)
    
    n_q = len(transTrans_Q)
    for i in range(n_q):
        row = []
        for j in range(n_q):
            if i == j:
                row.append(1.0)
                continue
            row.append(0.0)
        absorbant_I.append(row)
    return transTrans_Q, transAbsorbants_R, absorbant_I, absorbants

  
def compute_probs(m):
    for i in range(len(m)):
        den = sum(m[i])
        for j in range(len(m[i])):
            if m[i][j] != 0:
                m[i][j] =  float(m[i][j]) / den
    return m
            
def simplify(m):
    simp = []
    for i in range(len(m)):
        row = []
        for j in range(len(m[i])):
            row.append(Fraction(m[i][j]).limit_denominator())
        simp.append(row)
    return simp
    

def solution(m):
   m = compute_probs(m)
   Q,R,I,absorbants = standardize(m)
   if len(absorbants) == len(m):
       return [1,1]
   I_Q = numpy.subtract(I, Q)
   I_Q_ = numpy.linalg.inv(I_Q)
   I_Q_multi_R = numpy.dot(I_Q_, R)
   simped = simplify(I_Q_multi_R)
   l = []
   lcM = lcm(simped[0])
   for s in simped[0]:
       l.append( lcM/s.denominator * s.numerator)
   l.append(lcM)
   return l
    
# s = solution([
#   [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
#   [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
#   [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
#   [0,0,0,0,0,0],  # s3 is terminal
#   [0,0,0,0,0,0],  # s4 is terminal
#   [0,0,0,0,0,0],  # s5 is terminal
# ])

# s = solution([
#     [0, 2, 1, 0, 0], 
#     [0, 0, 0, 3, 4], 
#     [0, 0, 0, 0, 0], 
#     [0, 0, 0, 0,0], 
#     [0, 0, 0, 0, 0]
# ])

s = solution([
     [0, 1, 0, 0, 0, 1],
     [4, 0, 0, 3, 2, 0], 
     [0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0]
])

print(s)