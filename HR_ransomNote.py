#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    isUsable = False
    if len(magazine) > len(note):
        for no in note:
            if no in magazine:
                magazine.remove(no)
                isUsable = True
            else: 
                isUsable = False
                break
    print ('Yes' if isUsable else 'No')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
