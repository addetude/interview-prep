class Solution(object):
    def returnToBoundaryCount(self, nums):
        steps = 0
        count = 0
        for i in range(len(nums)):
            steps += nums[i]
            if steps == 0:
                count += 1
        return count
        