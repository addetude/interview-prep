class Solution(object):
    def sortedSquares(self, nums):
        l = []
        for num in nums:
            l.append(num*num)
        
        return sorted(l)
        