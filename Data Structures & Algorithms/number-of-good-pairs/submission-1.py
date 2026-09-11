class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        p = 0

        for n in nums:
            if n in count:
                p += count[n]
            count[n] = count.get(n,0)+1
        return p