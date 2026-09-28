class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        av = Counter(chars)
        a = 0
        for w in words:
            n = Counter(w)
            good = True
            for c in n:
                if n[c] > av[c]:
                    good = False
            if good:
                a += len(w)
        return a