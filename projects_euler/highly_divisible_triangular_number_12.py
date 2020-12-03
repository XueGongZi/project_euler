import largest_prime_factor_3 as prime
import math

class Solution:
    def highest_power(self, num, prime):
        i = 1
        while prime ** i < num and num % (prime ** i) == 0:
            i += 1
        return i - 1

    def number_of_divisors(self, num):
        power = 0.5
        square_root = math.floor(num ** power)
        factor_array = []
        for i in range(2, square_root + 1):
            if num % i == 0:
                divisor = num // i
                if prime.Solution().is_prime(i):
                    factor_array.append(i)
                if prime.Solution().is_prime(divisor):
                    factor_array.append(divisor)
        number = 1
        for i in factor_array:
            number *= self.highest_power(num, i) + 1
        return number - 1

    def highly_divisible_triangular_number(self, limit):
        i = 28
        j = 7
        while self.number_of_divisors(i) <= limit:
            j += 1
            i += j
        return i

