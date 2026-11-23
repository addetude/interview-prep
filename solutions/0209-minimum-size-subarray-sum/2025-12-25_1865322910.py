class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = r = summ = 0
        minLen = 1000000

        while r < len(nums):
            summ += nums[r]
            if summ >= target:
                minLen = min(minLen, r - l + 1)
                summ -= nums[l]
                l += 1
                summ -= nums[r]
            else:
                r += 1
                
        if minLen == 1000000:
            return 0
        return minLen
        