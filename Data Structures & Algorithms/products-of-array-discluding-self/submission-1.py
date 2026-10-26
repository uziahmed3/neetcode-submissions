class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # PREFIX: Calculate the product of all numbers to the LEFT
        p = 1

        # Loop from left to right
        for i in range(len(nums)):
            result[i] *= p  # Store the product of numbers before i
            p *= nums[i]    # Update p by multiplying the current number

        # SUFFIX: Calculate the product of all numbers to the RIGHT
        s = 1

        # Loop from right to left
        for i in range(len(nums)-1, -1, -1):
            result[i] *= s  # Multiply by the product of numbers after i
            s *= nums[i]    # Update s by multiplying the current number

        # Return the final array
        return result