class Solution:
    def largestGoodInteger(self, num: str) -> str:
        m = -1

        for i in range(2,len(num)):
            if num[i] == num[i-1] and num[i] == num[i-2]:
                m = max(m,int(num[i]))

        if m == -1:
            return ""
 

        return str(m) * 3