class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        k = 0
        for i in range(len(heights)):
            if heights[i] != s[i]:
                k += 1
        return k