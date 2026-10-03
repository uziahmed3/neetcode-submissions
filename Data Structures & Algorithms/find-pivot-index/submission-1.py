class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t = sum(nums)
        l = 0

        for i in range(len(nums)):
            r = t - l
            l += nums[i]
            if l == r:
                return i
        return -1