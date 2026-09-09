class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2*len(nums))
        i = 0

        for num in nums:
            ans[i] = num
            i += 1
        for num in nums:
            ans[i] = num
            i += 1
        return ans