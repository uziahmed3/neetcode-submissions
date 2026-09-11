class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        g = -1

        for i in range(len(arr) - 1, -1,-1):
            c = arr[i]
            arr[i] = g
            g = max(g,c)
        return arr