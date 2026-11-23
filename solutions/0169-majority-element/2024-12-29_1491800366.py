class Solution(object):
    def majorityElement(self, nums):
        count = 0
        ans = -1

        for elem in nums:
            if count == 0:
                ans = elem

            if ans == elem:
                count += 1
            else:
                count -= 1
        return ans
        
        