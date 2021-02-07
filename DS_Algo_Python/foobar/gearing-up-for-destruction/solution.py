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

    if nR == 0 or sR < 1:
        return -1

    return 1

def solution(pegs):

    n = len(pegs)
    sol = 0
    if n == 2:
        x = pegs[1] - pegs[0]
        sol = float(x) / 3
        sol = abs(sol * 2)
    else:
        i = n - 1
        subs = []
        s = 0
        while i > 0:
            m = pegs[i] - pegs[i-1]
            subs.append(m)
            i-=1
        i = 1
        s = subs[0]
        subtract = False
        while i < len(subs):
            subtract = not subtract
            if subtract:
                s = s - subs[i]
            else:
                s = s + subs[i]
            i += 1

        if subtract:
            sol = abs(s * 2)
        else:
            sol = float(s) / 3
            sol = abs(sol * 2)
    

    if sol == -1 :
        return [-1,-1]
        

    f = Fraction(sol).limit_denominator()
    if f < 2:
        return [-1,-1]

    sol2 = check(pegs,f)
    if sol2 == -1:
        return [-1,-1]
    
    return [f.numerator,f.denominator]

print(solution([4,30,50]))
print(solution([1,4]))
print(solution([3,27,97,149]))