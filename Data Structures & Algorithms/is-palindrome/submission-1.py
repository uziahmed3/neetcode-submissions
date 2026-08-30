class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())

        b = 0
        e = len(s) - 1

        while b < e:
            if s[e] == s[b]:
                e -= 1
                b += 1
            else:
                return False
        return True
