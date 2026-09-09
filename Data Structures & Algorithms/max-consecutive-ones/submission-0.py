class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        m = 0
        i = 0

        while i < n:
            if nums[i] != 1:
                l = 0
                i += 1
            else:
                l += 1
                m = max(m, l)
                i += 1
        return m

             