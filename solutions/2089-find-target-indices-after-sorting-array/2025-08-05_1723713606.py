class Solution(object):
    def targetIndices(self, nums, target):
        nums = sorted(nums)
        arr = []

        for i, num in enumerate(nums):
            if num == target:
                arr.append(i)
            
        return arr
        