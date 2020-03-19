# Problem 7, 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10 001st prime number?
import math_definition as math

limit = 10001

def list_of_primes_with_length_n(n):
    list_of_primes = [2]
    natural_number = 3
    while len(list_of_primes) <= n:
        if math.is_prime(natural_number) and len(list_of_primes) + 1 > n:
            return list_of_primes
        elif math.is_prime(natural_number):
            list_of_primes.append(natural_number)
            natural_number += 1
        else:
            natural_number += 1
def ans():
    prime_number = list_of_primes_with_length_n(limit)[-1]
    return prime_number
