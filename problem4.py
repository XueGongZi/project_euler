# Problem 4, Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.

import math_definition as math

def smallest_n_digits(n):
    return 10 ** (n - 1)

def largest_n_digits(n):
    return 10 ** n - 1

lower_limit = smallest_n_digits(3) ** 2
uppler_limit = largest_n_digits(3) ** 2
number_of_digits = 3

def palindrome_and_products_of_n_digits(low, high, digits):
    n = high
    while n > low:
        if math.is_palindromic(n) and products_of_n_and_m_digits(digits, digits, n):
            return n
            break
        else:
            n -= 1
    return n

def product_list(number):
    round_number = round(number ** 0.5)
    factor = round_number - 1 if number ** 0.5 < round_number else round_number
    product = []
    while 1 < factor:
        if math.is_divisible(factor, number):
            product += [[factor, number // factor]]
        factor -= 1
    return product

def products_of_n_and_m_digits(n, m, number):
    products = product_list(number)[0]
    smaller_number, bigger_number = products[0], products[1]
    if math.is_n_digits_positive_number(n, smaller_number) and math.is_n_digits_positive_number(m, bigger_number):
        return True
    else:
        return False

def ans():
    return palindrome_and_products_of_n_digits(lower_limit, uppler_limit, number_of_digits)
