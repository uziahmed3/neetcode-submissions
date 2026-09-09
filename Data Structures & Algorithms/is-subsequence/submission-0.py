class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        a = len(s) - 1
        b = len(t) - 1
        i = 0
        j = 0

        while i <= a and j <= b:
            if s[i] != t[j]:
                j += 1
            else:
                i += 1
                j += 1
        return i == a + 1