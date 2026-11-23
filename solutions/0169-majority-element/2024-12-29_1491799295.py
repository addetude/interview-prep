class Solution(object):
    def majorityElement(self, nums):
        count = 0
        ans = -1

        for elem in nums:
            if elem == ans:
                count += 1
            else:
                if count == 0:
                    ans = elem
                else: count -= 1
        return ans
        
        