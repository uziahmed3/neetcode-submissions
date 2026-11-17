class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        r = [0] * len(nums)  

        p = 0  
        n = 1 

        for nu in nums:

            if nu > 0:
                r[p] = nu
                p += 2
            else:
                r[n] = nu
                n += 2
        return r