class Solution(object):
    def findMaxAverage(self, nums, k):
        l = 0
        summ = sum(nums[:k])
        maxAvg = summ / float(k)

        for i in range(k, len(nums)):
            summ -= nums[i - k]
            summ += nums[i]
            avg = summ / float(k)

            if avg > maxAvg:
                maxAvg = avg
            
        
        return maxAvg


        
        