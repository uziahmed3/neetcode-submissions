class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set()
        r = []

        for ro in grid:
            for n in ro:
                if n in s:
                    r.append(n)
                s.add(n)
        n = len(grid)
        for num in range(1, n ** 2 + 1):
            if num not in s:
                r.append(num)
        return r