# Problem 2, Even Fibonacci numbers
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import problem1 as math

math = math.find_sum_array

limit = 4000000

def new_fibonacci_term(array):
    last_term = array[-1]
    second_last_term = array[-2]
    return last_term + second_last_term

def construct_fibonacci_sequence_below(upper_limit):
    fibonacci_seq = [1, 1]
    while new_fibonacci_term(fibonacci_seq) < upper_limit:
        fibonacci_seq += [new_fibonacci_term(fibonacci_seq)]
    return fibonacci_seq

def ans():
    return math(construct_fibonacci_sequence_below(limit)) // 2 - 1
