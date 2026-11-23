class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        maxx = 0

        while l < r:
            area = (r - l)*(min(height[l],height[r]))
            if area > maxx:
                maxx = area
            
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        
        return maxx


        