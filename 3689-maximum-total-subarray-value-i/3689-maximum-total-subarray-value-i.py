class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        gMin = gMax = nums[0]

        for n in nums:
            gMin = min(gMin, n)
            gMax = max(gMax, n)
        
        return (gMax - gMin) * k