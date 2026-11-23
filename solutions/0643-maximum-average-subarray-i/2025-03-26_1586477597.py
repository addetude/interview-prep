class Solution(object):
    def findMaxAverage(self, nums, k):
        total = 0
        for i in range(k):
            total += nums[i]

        maximum = float(total)/k

        for i in range(k, len(nums)):
            total = total + nums[i] - nums[i - k]
            maximum = max(float(total)/k, maximum)

        return maximum

