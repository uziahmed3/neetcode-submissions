class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
            pairs = []

            for i in range(len(names)):
                pairs.append((heights[i], names[i]))
            pairs.sort(reverse= True) 
            r = []
            for h,n in pairs:
                r.append(n)
            return r         