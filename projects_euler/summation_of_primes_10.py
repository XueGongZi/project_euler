import largest_prime_factor_3 as prime

class Solution:
    def summation_of_primes(self, limit):
        # limit is the upper limit
        new_limit = limit // 6
        summ = 5
        for i in range(1, new_limit + 1):
            first = 6 * i - 1
            second = 6 * i + 1
            if first < limit and prime.Solution().is_prime(first):
                summ += first
            if second < limit and prime.Solution().is_prime(second):
                summ += second
        return summ

limit = 2000000
print(Solution().summation_of_primes(limit))
