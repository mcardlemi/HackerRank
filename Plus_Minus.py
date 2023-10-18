#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos=0
    neg=0
    zed=0
    for i in range(len(arr)):
        if (arr[i]==0):
            zed+=1
        elif(arr[i] <0):
            neg+=1
        else:
            pos+=1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zed/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
