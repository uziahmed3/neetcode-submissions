class Solution:
    def firstUniqChar(self, s: str) -> int:
        sc = Counter(s)
        a = 0
        m = 0
        for i in range(len(s)):
            if sc[s[i]] == 1:
               return i
        return -1

