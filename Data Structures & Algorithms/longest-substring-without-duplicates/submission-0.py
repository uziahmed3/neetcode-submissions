class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        si = set()
        m = 0
        l = 0
        for i in range(len(s)):
            while s[i] in si:
                si.remove(s[l])
                l += 1
            
            si.add(s[i])
            m = max(m,i-l+1)
        return m