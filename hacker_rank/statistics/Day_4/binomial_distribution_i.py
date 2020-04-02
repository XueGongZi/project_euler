class Solution:
    def binomial_distribution_less_than_or_equal(self, limit: int, p, total: int):
        def factorial(n):
            if n == 1 or n == 0:
                return 1
            else:
                return n * factorial(n - 1)
        def n_choose_m(n, m):
            return factorial(n) / (factorial(m) * factorial(n - m))
        def b_power_of_a(a, b):
            return a ** b
        def binomial_equal(k):
            result = n_choose_m(total, k) * b_power_of_a(p, k) * b_power_of_a(1 - p, total - k)
            return result
        arr = list(range(limit + 1))
        pb = sum(list(map(lambda x: binomial_equal(x), arr)))
        return pb

"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    prob = 1.09 / (1.09 + 1)
    result = round((1 - Solution().binomial_distribution_less_than_or_equal(2, prob, 6)), 3)
    
    fptr.write(str(result) + '\n')

    fptr.close()
"""
