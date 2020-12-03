import math

class Solution:
    def is_prime(self, num):
        upper_limit = math.ceil(num ** 0.5)
        lower_limit = 2
        if num == 2:
            return True
        else:
            for i in range(2, upper_limit + 1):
                if num % i == 0 and i < num:
                    return False
                    break
            return True

    def largest_prime_number(self, num):
        upper_limit = math.ceil(num ** 0.5)
        result = 2
        for i in range(2, upper_limit + 1):
            if num % i == 0 and self.is_prime(i):
                result = i
        return result

num = 600851475143
