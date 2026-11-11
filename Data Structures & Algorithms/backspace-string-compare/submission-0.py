class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sq = []  
        tq = []

        for a in s:
            if a == '#':
                if sq:
                    sq.pop()
            else:
                sq.append(a)
        for a in t:
            if a == '#':
                if tq:
                    tq.pop()
            else:
                tq.append(a)
        return sq == tq