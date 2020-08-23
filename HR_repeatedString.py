#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    
    count_per_substr = 0
    for ss in s:
        if ss == 'a':
            count_per_substr += 1
    
    substr_len = len(s)
    repetitions = int(n / substr_len)
    count += count_per_substr * repetitions
    remainder = int(n % substr_len)
    for ss in s[:remainder]:
        if ss == 'a':
            count += 1

    return count

if __name__ == '__main__':
    s = input()

    n = int(input())

    print(repeatedString(s, n))
