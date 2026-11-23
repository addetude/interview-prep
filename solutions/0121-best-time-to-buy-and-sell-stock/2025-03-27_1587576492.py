class Solution(object):
    def maxProfit(self, prices):
        maxP = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxP