class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        r = []

        for w in words:
            for o in words:
                if w in o and w != o:
                    r.append(w)
                    break
        return r
               