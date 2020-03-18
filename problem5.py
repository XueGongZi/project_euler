# Problem 5, Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math_definition as math
import numpy as np
limit = 20

def number_for_n_with_highest_power_within_m(n, m):
    p = 0
    while n ** p <= m:
        if n ** (p + 1) > m:
            return n ** p
        else:
            p += 1

def ans():
    list_of_primes = list(filter(math.is_prime, range(2, limit + 1)))
    list_of_multiplies = list(map(lambda x: number_for_n_with_highest_power_within_m(x, limit), list_of_primes))
    return np.prod(list_of_multiplies)
