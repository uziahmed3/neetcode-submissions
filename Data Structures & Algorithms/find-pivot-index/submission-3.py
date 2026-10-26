class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t = sum(nums)
        l = 0

        for i in range(len(nums)):
            r = t - l - nums[i]
            if r == l:
                return i
            l += nums[i]
        return -1
