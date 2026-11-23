class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        d = {}
        a = []
        sort = sorted(nums)
        for i in range(len(nums)):
            if not sort[i] in d:
                d[sort[i]] = i
        for num in nums:    
            a.append(d[num])

        return a