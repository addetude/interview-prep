class Solution(object):
    def twoSum(self, nums, target):
        mapp = {}
        for i, num in enumerate(nums):
            if num in mapp:
                return [i, mapp[num]]
            else:
                mapp[target - num] = i
            
        return []

        