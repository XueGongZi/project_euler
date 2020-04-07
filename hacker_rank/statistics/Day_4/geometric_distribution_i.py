# In this challenge, we learn about geometric distributions.
import os

class Solution:
    def geometric_distribution_equal(self, total: int, p):
        def b_power_of_a(a, b):
            return a ** b
        pb = b_power_of_a((1 - p), (total - 1)) * p
        return pb

"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    prob = 1 / 3
    result = round(Solution().geometric_distribution_equal(5, prob), 3)
    
    fptr.write(str(result) + '\n')

    fptr.close()
"""
