# Problem 3, Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?

import math_definition as math

target = 600851475143

def factor_list(number):
    if math.is_prime(number):
        list_of_factor = [number]
        return list_of_factor
    else:
        smallest_factor = math.smallest_factor(number)
        list_of_factor = [smallest_factor]
        while smallest_factor < (number // smallest_factor):
            number = number // smallest_factor
            smallest_factor = math.smallest_factor(number)
            list_of_factor += [smallest_factor]
    return list_of_factor

def ans():
    return factor_list(target)[-1]

