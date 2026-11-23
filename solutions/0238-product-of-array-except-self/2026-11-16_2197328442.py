class Solution(object):
    def productExceptSelf(self, nums):
        left_prod = 1
        right_prod = 1
        n = len(nums)
        res = []

        for i in range(n):
            res.append(left_prod)
            left_prod *= nums[i]

        for i in range(n-1, -1, -1):
            res[i] *= right_prod
            right_prod *= nums[i]
            


        return res
            


