class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        p = 0

        for n in nums:
            if n in count:
                p += count[n]
                count[n] += 1
            else:
                count[n] = 1
        return p