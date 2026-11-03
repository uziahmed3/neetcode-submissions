class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter("".join(words))
        w = len(words)
        for a in c.values():
            if a % w != 0:
                return False
        return True