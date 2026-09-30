class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        for c in arr:
            count[c] = count.get(c, 0) + 1
        i = 0
        for c in arr:
            if count[c] == 1:
                i += 1
            if i == k:
                return c
        return ""