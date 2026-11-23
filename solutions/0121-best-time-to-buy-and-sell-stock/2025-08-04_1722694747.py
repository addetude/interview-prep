class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        l,r = 0,1
        m = 0

        while r < len(prices):
            if prices[l] <= prices[r]:
                if prices[r] - prices[l] > m:
                    m = prices[r] - prices[l]
            else:
                l = r
            r += 1

        return m
        
        