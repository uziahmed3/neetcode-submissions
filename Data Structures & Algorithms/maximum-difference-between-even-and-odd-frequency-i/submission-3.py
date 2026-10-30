class Solution:
    def maxDifference(self, s: str) -> int:
        s = Counter(s)
        mo = 0
        me = float('inf')

        for freq in s.values():
            if freq % 2 == 0:
                me = min(me,freq)
            if freq % 2 != 0:
                mo = max(mo,freq)
        return mo-me