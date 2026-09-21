class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        m = -1

        for k, v in d.items():
            if int(k) == v:
                m = max(m,v)
        return m
