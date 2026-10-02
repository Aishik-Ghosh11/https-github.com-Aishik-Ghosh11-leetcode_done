class Solution:
    def jump_rec(self, nums, src_idx, dest_idx, dp):
        if src_idx == dest_idx:
            dp[src_idx] = 0
            return dp[src_idx]

        if dp[src_idx] != -1:
            return dp[src_idx]

        min_jump_to_reach_dest = float("inf")
        for jump in range(1, nums[src_idx] + 1):
            if src_idx + jump < len(nums):
                min_jump_to_reach_dest = min(min_jump_to_reach_dest, self.jump_rec(nums, src_idx + jump, dest_idx, dp))

        dp[src_idx] = min_jump_to_reach_dest + 1
        return dp[src_idx]

    def jump(self, nums: List[int]) -> int:
        cols = len(nums)
        dp = [-1] * cols
        
        return self.jump_rec(nums, 0, len(nums) - 1, dp)