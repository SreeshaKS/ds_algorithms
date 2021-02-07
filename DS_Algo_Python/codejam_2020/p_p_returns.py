#!/bin/python3

import os
import sys

def doesOverlap(a1,a2):
    b = False
    if a1[0] < a2[0] < a1[1] or a2[0] < a1[0] < a2[1]:
        b = True
    if a1[1] < a2[1] and a2[0] < a1[1]:
        b = True
    if a2[1] > a1[0] and a2[1] < a1[1]:
        b = True
    # print("a1", a1)
    # print("a2", a2)
    # print(b)
    return b

def isRight(actMap, acts, nActs):
    i = 0
    j = 0
    
    while i < nActs:
        j = 0
        while j != i and j < nActs:
            b = doesOverlap(acts[i], acts[j])
            #print(actMap,actMap[i],actMap[j], i, j,b)
            if b:
                if ( actMap[i] == 'C' and actMap[j] == 'C') or ( actMap[i] == 'J' and actMap[j] == 'J'):
                    return False
            j += 1
        i+=1
    return True

def soutionRecur(actMap, acts, nActs, cA):
    
    b = isRight(actMap, acts, nActs)
    # print(actMap,b)
    if not b:
        return False
    
    if cA == nActs and b:
        return True
    
    if actMap[cA] == "":
        if actMap[cA-1] == 'C':
            actMap[cA] = 'J'
        else:
            actMap[cA] = 'C'
    
    if doesOverlap(acts[cA], acts[cA-1] ):
        if actMap[cA-1] == 'C':
            actMap[cA] = 'J'
            b = soutionRecur(actMap, acts,nActs,cA +1)
            if b:
                return b
        if actMap[cA-1] == 'J':
            actMap[cA] = 'C'
            b = soutionRecur(actMap, acts,nActs,cA +1)
            if b:
                return b
    elif soutionRecur(actMap, acts,nActs,cA + 1 ):
        return True
    else:
        if actMap[cA] == 'C':
            actMap[cA] = 'J'
        else:
            actMap[cA] = 'C'
        return soutionRecur(actMap, acts,nActs,cA +1)
    
    # solution[cA] = actMap
    return False

def mapToList(m):
    return [m[a] for a in m]
    

# Complete the solve function below.
def solve( acts, nActs):
    l = []
    #print(nActs)
    #print(acts)
    actMap = {}
    actMap[0] = 'J'
    for i in range(nActs):
        if i != 0:
            actMap[i] = ""
    
    if soutionRecur(actMap,acts,nActs,1):
        l = mapToList(actMap)
    else:
        actMap[0] = 'C'
        if soutionRecur(actMap,acts,nActs,1):
            l = mapToList(actMap)
        else:
            return []
    
    return l

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nActs = int(input())
        acts = []
        for n in range(nActs):
            act = [int(a) for a in input().split(" ")]
            acts.append(act)

        y = solve(acts,nActs)
        if len(y) == 0:
            print("Case #{}: {}".format(t_itr+1,"IMPOSSIBLE"))
        else:
            print("Case #{}: {}".format(t_itr+1,"".join(y)))
