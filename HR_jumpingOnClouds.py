#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    total_jumps = 0
    curr_step = 0
    dest = len(c) - 1
    while curr_step != dest:
        if curr_step + 2 <= dest and c[curr_step + 2] == 0:
            curr_step += 2
            total_jumps += 1
        elif c[curr_step + 1] == 0:
            curr_step += 1
            total_jumps += 1
    return total_jumps

if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    print(jumpingOnClouds(c))
