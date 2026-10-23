class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        res = 0
        while l < n:
            for i in range(n):
                sub = nums[i: i+l+1]
                if len(sub) != l+1:
                    continue
                distinct = len(set(sub))
                res += distinct**2
            l += 1
        
        return res