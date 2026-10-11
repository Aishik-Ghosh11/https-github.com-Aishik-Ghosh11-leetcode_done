class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        idx = 0
        n = len(nums)

        for i in range(n):
            if n %  (i + 1) == 0:
                idx += nums[i] * nums[i]
        
        return idx