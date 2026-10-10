class Solution:
    def countSeniors(self, details: List[str]) -> int:
        a = 0

        for d in details:
            n = int(d[11:13])
            if n > 60:
                a += 1
        return a