# Problem 5, Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def number_for_n_with_highest_power_within_m(n, m):
    p = 0
    while n ** p <= m:
        if n ** (p + 1) > m:
            return n ** p
        else:
            p += 1

print(number_for_n_with_highest_power_within_m(2, 20))
