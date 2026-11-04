class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        length = 0
        odd = False

        for n in c.values():
            if n % 2 == 0:
                length += n
            else:
                length += n - 1
                odd = True

        if odd:
            length += 1

        return length