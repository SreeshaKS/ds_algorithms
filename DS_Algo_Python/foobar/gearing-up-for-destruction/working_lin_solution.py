from fractions import Fraction
import math

def check(pegs, sR):
    i = 0 
    n = len(pegs)
    nSR = sR
    nR = 0

    while i < n-1:
        diff = pegs[i+1] - pegs[i]

        nR = diff - nSR

        if nR < 1:
            return -1
            
        nSR = nR
        i += 1

    sRR = round(sR, 2)
    nRR = round(nR, 2)

    if nRR == 0:
        return -1

    r = sRR / nRR

    if r != 2.0:
        return -1

    return 1
    
def linsearch(lo, hi, pegs):
    factor = 1

    while lo <= hi:
        t = check(pegs,lo)

        if t == 1:
            return round(lo,2)

        lo += factor

    return -1

def solution(pegs):

    p1 = 1
    p2 = pegs[1] - pegs[0] - 1
    n = len(pegs)
    if n == 0 or n  == 1:
        return [-1,-1] 
    if p2 < 0:
        return [ -1, -1 ]
    
    sol = linsearch(p1,p2,pegs)

    if sol == -1:
        return [ -1, -1 ]
        
    R1 = Fraction(sol).limit_denominator()
    
    if sol > p2 - p1 or sol < 2:
        return [ -1, -1 ]
    
    if R1.numerator >= R1.denominator:
        return [R1.numerator, R1.denominator]
    else:
        return [ -1, -1 ]


print(solution([4,30,50]))
print(solution([1,11]))
print(solution([3,27,97,150,151,221,291,293]))
print(solution([3,27,97,149,151,221,291,293]))