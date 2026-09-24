class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        candidates = []
        for idx in range(len(nums)):
            digit_sum = sum([int(digit) for digit in str(nums[idx])])
            if idx == digit_sum:
                candidates.append(idx)

        return -1 if len(candidates) == 0 else min(candidates)