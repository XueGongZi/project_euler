# Complete the permutationEquation function in the editor below. It should return an array of integers that represent the values of y.

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    n = len(p)
    initial_arr = list(range(1, n + 1))
    mid_arr = list(map(lambda x: p.index(x) + 1, initial_arr))
    result = list(map(lambda x: p.index(x) + 1, mid_arr))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
