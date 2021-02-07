#!/bin/python3

import os
import sys


def addParans(num,p,s):
    i = 0
    lr = []
    while i < num:
        lr.append("(")
        i+=1
    if s:
        lr.append(str(p))
    i=0
    while i < num:
        lr.append(")")
        i+=1
    
    return lr

def insert(arr ,i, l):
    la = arr[0:i+1]
    la.extend(l)
    la.extend(arr[i+1:])
    return la

#(((3)))
def pushElem(arr, num): 
    n = len(arr)
    i = n - 1
    k = 0

    while k < num and i >= 0:
        
        if arr[i] != ")" and arr[i] != "(":
            #print("num encountered",k,i,arr,arr[i])
            x = addParans(num-k,num,True)
            
            return insert(arr,i,x)
        
        if arr[i] == ")":
            k += 1

        i -= 1
    if len(arr) == 0:
        #print("num encountered",k,i,arr,arr[i])
        x = addParans(num,num,True)
        
        return insert(arr,i,x)
    
    la = insert(arr,i,[str(num)])
    return la

# Complete the solve function below.
def solve(ds):
    M = max(a)
    r = addParans(M,0,False)
    r = []
    i = 0
    #print(r)
    while i < len(ds):
        if ds[i] == 0:
            #print(ds[i],i)
            if i == 0:
                t = ["0"]
                t.extend(r)
                r = t
               #print(r)
            else:
                r.append("0")
            #print("pusing",ds[i],r)
            i += 1
            continue
        
        r = pushElem(r, ds[i]) 
        #print("pusing",ds[i],r)
        i += 1
    
    return r

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        a = [int(i) for i in input()]
        y = solve(a)
        s = values = ''.join(y)
        print("Case #{}: {}".format( t_itr+1, s ) )

