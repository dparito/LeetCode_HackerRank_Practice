#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    shift = [q[ueue] - ueue - 1 for ueue in range(len(q))]
    print(shift)
    total_bribaries = 0
    for i in shift:
        if i > 2:
            total_bribaries = -1
            break
        else:
            if i > 0:
                total_bribaries += i
    print(total_bribaries if total_bribaries > 0 else 'Too chaotic')


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
