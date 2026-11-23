class Solution(object):
    def singleNumber(self, nums):

        if len(nums) == 1:
            return nums[0]

        nums = sorted(nums)
        one = 0
        two = 1

        while two < len(nums):
            if nums[one] != nums[two]:
                return nums[one]
            one += 2
            two += 2
        
        return nums[len(nums) - 1]
        