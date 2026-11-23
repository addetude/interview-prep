class Solution(object):
    def numberOfPoints(self, nums):
        l = []
        for car in nums:
            for num in range(car[0], car[1] + 1):
                if not num in l:
                    l.append(num)
        
        return len(l)
        