class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        index = 0
        for i in nums:
            if i != 0:
                nums[index] = i
                index += 1
        while index < len(nums):
            nums[index] = 0
            index += 1
