class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if ~n & 1: return True

        @cache
        def maxDiff(i: int, j: int) -> int:
            if i == j: return nums[i]
            return max(nums[i] - maxDiff(i + 1, j),
                       nums[j] - maxDiff(i, j - 1))

        return maxDiff(0, n - 1) >= 0