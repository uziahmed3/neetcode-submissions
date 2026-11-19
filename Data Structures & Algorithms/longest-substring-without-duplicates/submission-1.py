class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        si = set()
        m = 0
        l = 0
        a = 0
        for r in range(len(s)):
            while s[r] in si:
                si.remove(s[l])
                l += 1
            si.add(s[r])
            m = max(m,r-l+1)
        return m
      