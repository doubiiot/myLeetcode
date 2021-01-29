class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_cur = profit = 0
        low = prices[0]
        for p in prices:
            profit_cur = p - low
            #lose money
            if profit_cur > 0:
                profit += profit_cur
            low = p
        return profit
