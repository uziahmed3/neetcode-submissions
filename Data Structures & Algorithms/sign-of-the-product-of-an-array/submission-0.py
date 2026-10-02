class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for n in nums:
            p *= n
        if p < 0:
            return -1
        elif p > 0:
            return 1
        else:
            return 0