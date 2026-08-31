class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        m = 0

        while l < r:
            b = min(heights[l], heights[r])
            a = (r-l) * b
            if l < r and heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            m = max(m, a)
        return m
