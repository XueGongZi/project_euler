import math

class Solution:
    def special_pythagorean_triplet(self, total):
        result = []
        limit = math.ceil(total / 3)
        for i in range(1, limit):
            for j in range(i + 1, limit + limit):
                k = 1000 - i - j
                if i ** 2 + j ** 2 == k ** 2:
                    result = [i, j, k]
        return result

total = 1000
print(Solution().special_pythagorean_triplet(total))
