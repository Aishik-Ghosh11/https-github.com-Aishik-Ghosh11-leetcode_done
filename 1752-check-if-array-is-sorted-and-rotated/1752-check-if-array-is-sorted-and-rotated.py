class Solution:
    def check(self, nums: list[int]) -> bool:
        return sum(nums[i - 1] > nums[i] for i in range(len(nums))) < 2