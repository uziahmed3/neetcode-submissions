class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m = nums[0]
        s = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                s += nums[i]
            else:
                s = nums[i]
            m = max(m,s)
        return m

