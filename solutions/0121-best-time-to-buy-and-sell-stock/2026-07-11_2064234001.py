class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        n = len(prices)
        buy = sell = 0

        while sell < n - 1:
            sell += 1
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                if prices[sell] - prices[buy] > maxx:
                    maxx = prices[sell] - prices[buy]

        return maxx