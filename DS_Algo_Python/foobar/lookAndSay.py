#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumOfTheDigits' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY q as parameter.
#
# 1 11 21 1211 111221 312211

def genElement(element):
    prevElement = element[0] + "%"
    summation = 0
    res = ""
    l = len(prevElement)
    i = 1
    count = 1
    
    while i < l:
        if prevElement[i] != prevElement[i-1]:
            summation = summation + count + int(prevElement[i-1])
            res = res + str(count) + prevElement[i-1]
            current = prevElement[i]
            count = 1
        else:
            count += 1
        
        i+=1
    return (res,summation)

def sumOfTheDigits(q):
    n = 45
    seq = [("",0)] * n
    seq[0] = ("1",1)
    seq[1] = ("11",2)
    
    i = 2
    while i <= n:
        s = seq[i-1]
        seq[i] = genElement(s)
        i += 1
    
    res = []
    
    for j in q:
        res.append(seq[j-1][1])
    return res

    
