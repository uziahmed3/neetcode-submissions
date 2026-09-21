class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = Counter(nums)

        for freq in n.values():
            if freq % 2 != 0:
                return False
        return True