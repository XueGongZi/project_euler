class Solution:
    def sum_of_multiples(self, multiples, upper, lower):
        # multiples = [3, 5]
        # upper = 1000
        # lower = 1
        multiples_array = []
        for i in multiples:
            multiple_array = []
            for j in list(range(lower, upper + 1)):
                if j % i == 0:
                    multiple_array.append(j)
            multiples_array.append(multiple_array)
        result = sum(list(set(sum(multiples_array, []))))
        return result

multiples = [3, 5]
upper = 999
lower = 1
result = Solution().sum_of_multiples(multiples, upper, lower)
print(result)
