# In this challenge, we practice calculating standard deviation.
# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

import os
import sys

def standard_deviation(data):
    n = len(data)
    def mean(arr):
        return sum(arr) / n
    meu = mean(data)
    sum_of_squares = sum(list(map(lambda x: (x - meu) ** 2, data)))
    return round((sum_of_squares / n) ** 0.5, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    data = list(map(int, input().rstrip().split()))

    result = standard_deviation(data)
    
    fptr.write(str(result) + '\n')

    fptr.close()
