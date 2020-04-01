# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

from collections import Counter

class Solution:
    def singleNumber(self, nums: [int]) -> int:
        origin = Counter(nums)
        filtered = dict(filter(lambda elem: elem[1] == 1, origin.items()))
        return list(filtered)[0]

