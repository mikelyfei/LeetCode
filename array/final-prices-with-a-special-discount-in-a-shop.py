class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = prices.copy()
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                j = stack.pop()
                res[j] = prices[j] - p 
            stack.append(i)
        return res