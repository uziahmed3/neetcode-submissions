class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            l, d = e.split("@")
            n = ""

            for i in l:
                if i == '.':
                    continue
                elif i == '+':
                    break
                n += i
            em = n + "@" + d
            
            s.add(em)
        return len(s)