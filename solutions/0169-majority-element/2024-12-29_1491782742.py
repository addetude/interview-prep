class Solution(object):
    def majorityElement(self, nums):
        d = {}
        m = 0
        me = nums[0]
        for elem in nums:
            if not elem in d:
                d[elem] = 1
            else:
                d[elem] += 1
            if d[elem] > m:
                m = d[elem]
                me = elem
        return me
        
        