class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = len(nums) - 1

        return (nums[n] * nums[n-1]) - (nums[i]*nums[i+1])