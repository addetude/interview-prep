class Solution(object):
    def findMaxAverage(self, nums, k):

        summ = 0
        for i in range(k):
            summ += nums[i]
        
        max_avg = float(summ)/k

        for i in range(k,len(nums)):
            summ = summ + nums[i] - nums[i-k]
            avg = float(summ)/k
            max_avg = max(max_avg, avg)
        return max_avg

