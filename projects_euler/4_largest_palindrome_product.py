class Solution:
    def largest_palindrome_product(self, first, second):
        # first is an array, [lower 3-digit, upper 3-digit] 
        # second is an array, [lower 3-digit, upper 3-digit]
        left = 0
        right = 0
        product = 0
        for i in range(first[0], first[1] + 1):
            for j in range(second[0], second[1] + 1):
                result = i * j
                normal = list(str(result))
                reverse = list(str(result))[::-1]
                if normal == reverse and product < result:
                    product = result
        return product


print(Solution().largest_palindrome_product([100, 999], [100, 999]))
