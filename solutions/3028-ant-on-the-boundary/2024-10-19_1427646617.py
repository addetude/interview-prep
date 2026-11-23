class Solution(object):
    def returnToBoundaryCount(self, nums):
        steps = 0
        count = 0
        length = len(nums)
        for i in range(length):
            steps += nums[i]
            if steps == 0:
                count += 1
        return count
        