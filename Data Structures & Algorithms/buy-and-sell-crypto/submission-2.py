class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        max_profit = 0
        l, r = 0, 1

        while l <= length - 1 and r <= length - 1:
            if prices[r] - prices[l] < 0:
                l = r
                r += 1
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1

        return max_profit
