class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        lowest = prices[0]

        for p in prices:
            profit = p - lowest
            lowest = min(lowest,p)
            m = max(m,profit)
        return m