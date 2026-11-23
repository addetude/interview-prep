class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        for i, nums in enumerate(nums):
            n ^= i^nums

        return n
        