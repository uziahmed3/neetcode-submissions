class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        a = 0
        j = 0
        i = 0
        g.sort()
        s.sort() 

        while i < len(g) and j < len(s):

            if g[i] <= s[j]:
                a += 1
                i += 1
                j += 1
            else:
                j += 1

        return a