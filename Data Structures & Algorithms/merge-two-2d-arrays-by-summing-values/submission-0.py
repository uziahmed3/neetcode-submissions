class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}

        for id, val in nums1:
            d[id] = val

        for id, val in nums2:
            if id in d:
                d[id] += val
            else:
                d[id] = val
        r = []

        for id in sorted(d):
            r.append([id, d[id]])
        return r


