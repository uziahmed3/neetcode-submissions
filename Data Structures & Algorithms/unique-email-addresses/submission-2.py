class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            l, d = e.split("@")
            n = ""
            for a in l:
                if a == ".":
                    continue
                if a == "+":
                    break
                n += a
            em = n + "@" + d
            s.add(em)
        return len(s)