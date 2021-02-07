#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(m,n):
    i, j = 0, 0
    trace = 0
    rr = 0
    rc = 0
    while i < n:
        #compute the trace
        trace += m[i][i]
        # check if row has repeated elements
        s = set(m[i])
        if len(s) < n:
            rr += 1
        
        #check if column has repeated elements
        col = []
        while j < n:
            col.append(m[j][i])
            j+=1
        j = 0
        if len(set(col)) < n:
            rc += 1
        
        i+=1
    return trace,rr,rc

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        i = 0
        matrix = []
        while i < n:
           matrix.append([int(s) for s in input().split(" ")])
           i+=1
        trace,rr,rc = solve(matrix,n)
        print("Case #{}: {} {} {}".format(t_itr+1,trace, rr,rc))
