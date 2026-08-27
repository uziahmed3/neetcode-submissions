class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)

        result = []

        for x, y in n.most_common(k):
            result.append(x)
        return result