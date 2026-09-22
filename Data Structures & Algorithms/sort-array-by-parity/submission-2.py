class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] % 2 == 0:
                l += 1
            elif nums[r] % 2 != 0:
                r -= 1
            else:

                t = nums[r]
                nums[r] = nums[l]
                nums[l] = t
                l += 1
                r -= 1

        return nums