#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(a, w):
    print(a,w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        w = list(map(int, input().rstrip().split()))

        result = solve(a, w)

        fptr.write(str(result) + '\n')

    fptr.close()
