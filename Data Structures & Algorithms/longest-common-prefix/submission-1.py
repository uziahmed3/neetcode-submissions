class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            for w in strs[1:]:
                if i >= len(w) or first[i] != w[i]:
                    return first[:i]
        return first


            