class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0

        l = 0
        r = 1
        maxx = 0
        
        while r < n:
            buy = prices[l]
            sell = prices[r]
            if buy >= sell:
                l += 1
                r = l + 1
            else:
                if (sell - buy) > maxx:
                    maxx = sell - buy
                r += 1
            
        return maxx

            