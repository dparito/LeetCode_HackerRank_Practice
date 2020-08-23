#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    arr_len = len(a)
    if d > arr_len:
        d = d % arr_len
    
    for i in range(d):
        popped = a.pop(0)
        a.append(popped)
    return a

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print (result)
