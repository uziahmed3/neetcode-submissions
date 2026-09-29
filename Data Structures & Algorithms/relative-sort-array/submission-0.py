class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        r = []

        for num in arr2:
            for i in range(count[num]):
                r.append(num)
        arr1.sort()
        for num in arr1:
            if num not in arr2:
                r.append(num)
        return r
