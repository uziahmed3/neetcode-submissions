class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            r -= 1
            l += 1
        return True