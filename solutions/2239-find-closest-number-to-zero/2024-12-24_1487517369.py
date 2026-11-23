class Solution(object):
    def findClosestNumber(self, nums):
        m = nums[0]
        absmin = abs(nums[0])
        for num in nums:
            absnum = abs(num)
            if absnum < absmin:
                m = num
                absmin = abs(num)
            elif absnum == absmin:
                if num > m:
                    m = num
                    absmin = abs(num)
        return m

        