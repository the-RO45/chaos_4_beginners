#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def cutTheSticks(arr):
    # Write your code here
    n=len(arr)
    ans=[]
    ans.append(n)
    while(n>=1):
        rmin=min(arr)
        new_arr=[]
        for i in range(0,n):
            arr[i]=arr[i]-rmin
            if arr[i]!=0:
                new_arr.append(arr[i])
        # print(new_arr)
        n=len(new_arr)
        ans.append(n)
        arr=new_arr
    ans.remove(0)
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
