class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        z = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[z-1]:
                nums[z] = nums[i]
                z += 1
        return z