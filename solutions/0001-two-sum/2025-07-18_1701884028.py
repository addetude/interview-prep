class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [i,d[nums[i]]]
            else:
                d[target - nums[i]] = i 
