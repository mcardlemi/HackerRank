#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour24 = s.split(":",3)
    if (hour24[2][2:] == "PM") and (hour24[0]!="12"):
        hour24[0] = str(int(hour24[0])+12)
    elif (hour24[2][2:] == "AM") & (hour24[0]=="12"):
        hour24[0] = "00"
    else:
        pass
    return hour24[0]+":"+hour24[1]+":"+hour24[2][:2]
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
