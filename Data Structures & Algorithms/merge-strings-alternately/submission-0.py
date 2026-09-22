class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a,b = 0,0
        r = []

        while a < len(word1) and b < len(word2):
            r.append(word1[a])
            r.append(word2[b])
            a += 1
            b += 1
        while a < len(word1):
            r.append(word1[a])
            a += 1
        while b < len(word2):
            r.append(word2[b])
            b += 1
        return "".join(r)
        