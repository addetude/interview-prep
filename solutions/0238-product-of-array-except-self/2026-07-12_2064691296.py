import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n

        running = 1
        for i, num in enumerate(nums):
            answer[i] *= running
            running *= num

        running = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= running
            running *= nums[i]

        return answer

        

