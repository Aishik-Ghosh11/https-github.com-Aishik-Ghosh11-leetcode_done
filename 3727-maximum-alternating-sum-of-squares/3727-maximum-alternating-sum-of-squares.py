class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [abs(n) for n in nums]
        nums.sort()
        score = 0
        idx = 0

        while idx < len(nums):
            sq = nums[idx] * nums[idx]
            if idx < int(len(nums)/2):
                score -= sq
            else:
                score += sq
            idx += 1
        
        return score
        