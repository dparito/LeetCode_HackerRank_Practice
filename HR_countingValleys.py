#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    num_valleys = 0
    trajectory = 0

    for direction in s:
        if direction == 'U':
            trajectory += 1
        else:
            if trajectory == 0:
                num_valleys += 1
            trajectory -= 1
    
    return num_valleys


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    print(countingValleys(n, s))

    # fptr.write(str(result) + '\n')

    # fptr.close()
