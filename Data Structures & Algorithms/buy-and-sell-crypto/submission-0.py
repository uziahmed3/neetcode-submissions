class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        lowest = prices[0]
        for p in prices:
            lowest = min(lowest,p)
            profit = p - lowest
            m = max(m,profit)
        return m

