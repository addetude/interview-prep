class Solution(object):
    def triangleType(self, nums):
        nums = sorted(nums)
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        nums = set(nums)
        n = len(nums)
        if n == 1:
            return "equilateral"
        elif n == 2:
            return "isosceles"
        return "scalene"
        