class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        longest = 0
        m = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            m = max(m,count[s[r]])

            while (r -l + 1) - m > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r-l +1)

        return longest