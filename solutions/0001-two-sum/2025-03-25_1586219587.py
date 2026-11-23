class Solution(object):
    def twoSum(self, nums, target):
        # difference:index
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                return [i,h[nums[i]]]
            else:
                h[target - nums[i]] = i
            
        

        