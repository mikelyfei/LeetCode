class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = float('inf')
        max_profit = - float('inf')
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)
        return max_profit