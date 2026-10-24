class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for w in strs:
            key = tuple(sorted(w))

            if key in groups:
                groups[key].append(w)
            else:
                groups[key] = [w]
        return list(groups.values())

