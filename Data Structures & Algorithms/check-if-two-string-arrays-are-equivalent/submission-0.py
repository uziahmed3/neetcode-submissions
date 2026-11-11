class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = []
        b = []

        for w in word1:
            for q in w:
                a.append(q)

        for w in word2:
            for q in w:
                b.append(q)
        return a == b