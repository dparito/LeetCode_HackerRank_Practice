#!/bin/python3

import math
import os
import random
import re
import sys

def get_hg_sum(hg) -> int:
    hg_sum = 0
    for ele in hg:
        hg_sum += ele
    return hg_sum

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum = -64
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            hg = [arr[i][j], arr[i][j+1], arr[i][j+2], arr[i+1][j+1], arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]
            hg_sum = get_hg_sum(hg)
            if hg_sum > sum:
                sum = hg_sum
    return sum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hourglassSum(arr))
