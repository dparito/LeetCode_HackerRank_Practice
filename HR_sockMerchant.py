#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar_dict = {}
    for a in ar:
        if a in ar_dict.keys():
            ar_dict[a] += 1
        else:
            ar_dict[a] = 1
    
    pairs = 0
    for k in ar_dict.keys():
        pairs += int(ar_dict[k] / 2)
    return pairs


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
