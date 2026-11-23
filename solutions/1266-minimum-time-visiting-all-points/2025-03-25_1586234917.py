class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        time = 0
        for i in range(len(points) - 1):
            xdif = abs(points[i+1][0] - points[i][0])
            ydif = abs(points[i+1][1] - points[i][1])
            time += max(xdif,ydif)
        return time

        