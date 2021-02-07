from fractions import Fraction
import math

def check(pegs, sR):
    i = 0 
    n = len(pegs)
    nSR = sR
    nR = 0
    #print(nSR)
    while i < n-1:
        diff = pegs[i+1] - pegs[i]
        if diff < 0:
            return -1
        nR = diff - nSR
        if nR < 0:
            return -1
        nSR = nR
        i += 1

    # r = math.ceil(float(sR) / nR)
    r = float(sR) / nR
    print(sR,nR,r)
    if r == 2.0:
        return 1
    if r < 2.0:
        return -1
    if r > 2.0:
        return 2
    return 2
    


def binsearch(lo, hi, pegs):
    sols = []
    while lo < hi:
        #mid = float( lo + hi ) / 2
        mid = (lo + hi) / 2
        t = check(pegs,mid)
        if t == 1:
            sols.append(mid)
            continue
        if t < 0:
            hi = mid
        else:
            lo = mid + 1
    return -1

def solution(pegs):
    p1 = 1
    p2 = pegs[1] - pegs[0] - 1
    if p2 < 0:
        return [-1,-1]
    #print(p1,p2)
    sol = binsearch(p1,p2,pegs)
    return sol
    # if sol == -1:
    #     return [-1,-1]

    # l = str(Fraction(sol)).split("/")
    # for i in range(len(l)):
    #     l[i] = int(l[i])
    
    # if len(l) == 1:
    #     return [l[0],1]
    # return l
    

print(solution([4,40,70]))
print(solution([4,30,50]))