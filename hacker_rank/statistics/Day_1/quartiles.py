# In this challenge, we practice calculating quartiles.
# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

import os
import sys

def quartiles(data):
    data.sort()
    length = len(data)
    def is_even(arr):
        return len(arr) % 2 == 0
    def is_integer(number):
        if int(number) == number:
            return int(number)
        else:
            return number
    def median(arr):
        length = len(arr)
        index = length // 2
        if is_even(arr):
            return is_integer((arr[index] + arr[index - 1]) / 2)
        else:
            return is_integer(arr[index])
    index = length // 2
    lower = data[:index]
    if is_even(data):
        upper = data[index:]
    else:
        upper = data[(index + 1):]
    first_quartile = median(lower)
    second_quartile = median(data)
    third_quartile = median(upper)
    return [first_quartile, second_quartile, third_quartile]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    result = quartiles(arr)
    
    for i in result:
        fptr.write(str(i) + '\n')

    fptr.close()


