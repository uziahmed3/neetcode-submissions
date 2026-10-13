class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        m = -1

        for f,i in d.items():
            if f == i:
                m = max(m,f)
        return m
