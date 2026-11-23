class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        first = 0
        last = k - 1
        summ = 0

        # load the window
        for i in range(k):
            summ += nums[i]

        maxx = summ
        
        while last < n - 1:
            summ -= nums[first]
            summ += nums[last + 1]

            if summ > maxx:
                maxx = summ

            first += 1
            last += 1

        return maxx/k
