#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

'''
    Problem: https://www.hackerrank.com/challenges/one-week-preparation-kit-jesse-and-cookies/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-six
    Question:
        1. Can we assume A to be sorted? Assuming no
        2. Solution ->
            https://programs.programmingoneonone.com/2021/05/hackerrank-jesse-and-cookies-solution.html
'''
def cookies(k, A):
    if not A:
        return -1
    A.sort() # confirm it sorts in asc
    
    ans = 0
    
    while A[0] < k and len(A) >=2 :
        ans += 1
        # take to smallest
        smallest = A[:2]
        new_val = smallest[0] + 2 * smallest[1]
        if len(A) > 2:
            A = [new_val] + A[2:]
        else:
            A = [new_val]
        A.sort()
    if A[0] >= k:
        return ans
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
