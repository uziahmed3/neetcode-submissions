class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        p = 1
        for i in range(len(nums)):
            result[i] = p
            p *= nums[i] 

        s = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= s
            s *= nums[i]
        return result