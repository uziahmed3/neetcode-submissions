class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        l = 0
        m = float("inf")

        for r in range(len(blocks)):
            if blocks[r] == "W":
                w += 1
            if r - l + 1 == k:
                m = min(w,m)
                if blocks[l] == "W":
                    w -= 1
                l += 1 
            
        return m
  
