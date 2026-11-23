class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        maxFill = (r - l)*min(height[l], height[r]) 

        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            newMax = (r - l)*min(height[l], height[r]) 
            if newMax > maxFill:
                maxFill = newMax
        
        return maxFill
        