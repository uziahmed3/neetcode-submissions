class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        for e in emails:
            local, domain = e.split("@")
            new_local = ""

            for c in local:
                if c == ".":
                    continue

                if c == "+":
                    break

                new_local += c

            email = new_local + "@" + domain
            s.add(email)

        return len(s)