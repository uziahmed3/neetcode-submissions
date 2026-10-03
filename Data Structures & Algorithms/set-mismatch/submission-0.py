class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        r = []
        for i in range(len(nums)):
            if nums[i] in seen:
                r.append(nums[i])
            seen.add(nums[i])
        for n in range(1, len(nums) + 1):
            if n not in seen:
                r.append(n)
        return r
