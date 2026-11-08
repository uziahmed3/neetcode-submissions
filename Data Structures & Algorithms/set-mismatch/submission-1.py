class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        r = []
        for i in range(len(nums)):
            if nums[i] in seen:
                r.append(nums[i])
            else:
                seen.add(nums[i])
        for i in range(1, len(nums) + 1):
            if i not in seen:
                r.append(i)
        return r
