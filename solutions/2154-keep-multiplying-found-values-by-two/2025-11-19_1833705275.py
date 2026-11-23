class Solution(object):
    def findFinalValue(self, nums, original):

        res = True
        while res:
            res = self.linSearch(nums, original)
            if not res:
                return original
            original *= 2

    def linSearch(self, nums, target):
        for num in nums:
            if num == target:
                return True
        
        return False
        