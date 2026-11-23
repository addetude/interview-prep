class Solution(object):
    def majorityElement(self, nums):
        d = {}
        l = len(nums) // 2 + 1
        for elem in nums:
            if not elem in d:
                d[elem] = 1
            else:
                d[elem] += 1
                if d[elem] == l:
                    return elem
        return nums[0]
        
        