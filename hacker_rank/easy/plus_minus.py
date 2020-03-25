# Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.

def plusMinus(arr):
    n = len(arr)
    zero_numbers = len(list(filter(lambda x: x == 0, arr)))
    positive_numbers = len(list(filter(lambda x: x > 0, arr)))
    negative_numbers = n - zero_numbers - positive_numbers

