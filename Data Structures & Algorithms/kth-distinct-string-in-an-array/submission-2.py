class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        for c in arr:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        i = 0
        for c in arr:
            if count[c] == 1:
                i += 1
            if k == i:
                return c
            
        return ""