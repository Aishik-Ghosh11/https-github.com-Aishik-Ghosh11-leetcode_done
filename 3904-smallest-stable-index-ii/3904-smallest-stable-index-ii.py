class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        prefix = [nums[0]] * n
        suffix = [nums[n-1]] * n

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], nums[i])
            suffix[n-i-1] = min(suffix[n-i], nums[n-i-1])

        for i in range(n):
            if prefix[i] - suffix[i] <= k:
                return i

        return -1


        