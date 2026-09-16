class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        al = set(allowed)
        a = 0

        for w in words:
            v = True
            for c in w:
                if c not in al:
                    v = False
            if v:
                a += 1
        return a