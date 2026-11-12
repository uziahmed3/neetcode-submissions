class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        r = []  
        j = 0 

        for i in range(len(s)):

            if j < len(spaces) and i == spaces[j]:
                r.append(" ")
                r.append(s[i])
                j += 1
            else:
                r.append(s[i])
        return "".join(r)
