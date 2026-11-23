class Solution(object):
    def containsDuplicate(self, nums):
        sett = set(nums)
        return len(sett) != len(nums)
        
        