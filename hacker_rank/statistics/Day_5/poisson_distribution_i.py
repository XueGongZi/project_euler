class Solution:
    def poisson_distribution_equal_k_and_average(self, k: int, a):
        e = 2.71828
        def factorial(n):
            if n == 1 or n == 0:
                return 1
            else:
                return n * factorial(n - 1)
        def b_power_of_a(a, b):
            return a ** b
        pb = b_power_of_a(a, k) * b_power_of_a(e, (-a)) / factorial(k)
        return pb

"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    prob = 1.09 / (1.09 + 1)
    result = round((1 - Solution().binomial_distribution_less_than_or_equal(2, prob, 6)), 3)
    
    fptr.write(str(result) + '\n')

    fptr.close()
"""
