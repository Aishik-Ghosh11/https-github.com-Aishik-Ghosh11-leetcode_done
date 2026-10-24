class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        low = min(nums)
        high = max(nums)

        cnt = [0] * (high - low + 1)
        for v in nums:
            cnt[v - low] += 1
        
        sorted_nums = []
        ans = []
        inner = 0
        for i, c in enumerate(cnt):
            if target == i + low:
                for _ in range(c):
                    ans.append(inner)
                    inner += 1
            sorted_nums.extend([i + low] * c)
            inner += c

        return ans