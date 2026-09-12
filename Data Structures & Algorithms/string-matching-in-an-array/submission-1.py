class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        r = []

        for w in words:
            for o in words:
                if w != o and w in o:
                    r.append(w)
                    break
        return r