class Solution(object):
    def moveZeroes(self, nums):

        l = 0

        while l < len(nums):
            if nums[l] == 0:
                nums.remove(0)
                nums.append(0)
            l += 1
        return nums
        