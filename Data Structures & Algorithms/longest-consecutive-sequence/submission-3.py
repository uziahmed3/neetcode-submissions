class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        m = 0

        for num in n:
            if num - 1 in n:
                continue
            else:
                a = 1
                while num + a in n:
                    a += 1
                m = max(m,a)
        return m
