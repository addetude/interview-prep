class Solution(object):
    def runningSum(self, nums):
        sum = 0
        array = []
        for i in range(len(nums)):
            sum += nums[i]
            array.append(sum)
        return array