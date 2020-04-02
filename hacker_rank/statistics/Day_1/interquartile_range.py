# In this challenge, we practice calculating the interquartile range.
# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

import os
import sys

def interquartile_range(elements, frequency):
    data = []
    for i in list(range(len(elements))):
        e = elements[i]
        index_arr = list(range(frequency[i]))
        element_arr = list(map(lambda _: e, index_arr))
        data += element_arr
    data.sort()
    length = len(data)
    def is_even(arr):
        return len(arr) % 2 == 0
    def median(arr):
        length = len(arr)
        index = length // 2
        if is_even(arr):
            return (arr[index] + arr[index - 1]) / 2
        else:
            return arr[index]
    index = length // 2
    lower = data[:index]
    if is_even(data):
        upper = data[index:]
    else:
        upper = data[(index + 1):]
    first_quartile = median(lower)
    third_quartile = median(upper)
    return "{:.1f}".format(third_quartile - first_quartile)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    elements = list(map(int, input().rstrip().split()))
    
    frequency = list(map(int, input().rstrip().split()))

    result = interquartile_range(elements, frequency)
    
    fptr.write(str(result) + '\n')

    fptr.close()
