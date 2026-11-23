class Solution(object):
    def twoSum(self, nums, target):
        # value2 : index of value 1 
        h = {}

        for i in range(len(nums)):
            if nums[i] in h:
                return [i,h[nums[i]]]
            else:
                h[target - nums[i]] = i

            
        

        