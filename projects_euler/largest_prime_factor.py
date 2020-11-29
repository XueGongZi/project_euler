import math

class Solution:
    def is_prime(self, num):
        upper_limit = math.ceil(num ** 0.5)
        lower_limit = 2
        if num == 2:
            return True
        else:
            for i in range(2, upper_limit + 1):
                

