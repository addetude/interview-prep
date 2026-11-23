class Solution(object):
    def minOperations(self, nums, k):
        summ = 0

        for i, num in enumerate(nums):
            summ += num

        return summ % k
        

        