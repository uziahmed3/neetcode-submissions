class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for w in words[1:]:
            common &= Counter(w)

        return list(common.elements())