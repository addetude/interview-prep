class Solution(object):
    def minOperations(self, nums, k):
        summ = sum(nums)

        return summ % k


        