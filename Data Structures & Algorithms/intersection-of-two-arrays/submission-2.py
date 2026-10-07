class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        r = set()

        for n in nums1:
            if n in s2:
                r.add(n)
        
        return list(r)