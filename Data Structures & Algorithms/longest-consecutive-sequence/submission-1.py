class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        m = 0

        for num in n:
            if num - 1 in n:
                continue
            l = 0
            while num + 1 in n:
                l += 1
                num += 1
            m = max(m,l+1)

        return m
