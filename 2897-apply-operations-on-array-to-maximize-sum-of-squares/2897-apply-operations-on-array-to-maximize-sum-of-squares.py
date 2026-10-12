class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        for num in nums:
            for b in range(32):
                if num & (1 << b):
                    bit_counts[b] += 1
        
        final_nums = [0] * len(nums)
        for i in range(len(nums)):
            val = 0
            for b in range(32):
                if bit_counts[b] > 0:
                    val |= (1 << b)
                    bit_counts[b] -= 1
            final_nums[i] = val
        
        final_nums.sort(reverse=True)
        ans = 0
        for i in range(k):
            ans = (ans + final_nums[i] * final_nums[i]) % MOD
        return ans