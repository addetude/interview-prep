class Solution(object):
    def twoSum(self, nums, target):
        
        # key: value searching for, value: index
        m = {}

        for i, n in enumerate(nums):
            if n in m:
                return [i, m[n]]
            m[target-n] = i

        
        return []



        