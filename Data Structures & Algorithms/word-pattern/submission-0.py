class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        d1 = {}
        d2 = {}

        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]

            if letter in d1:
                if d1[letter] != word:
                    return False
            else:
                d1[letter] = word

            if word in d2:
                if d2[word] != letter:
                    return False
            else:
                d2[word] = letter

        return True