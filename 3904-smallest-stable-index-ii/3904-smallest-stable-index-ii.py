class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        msf = -1
        cand = cm = 0

        for i, x in enumerate(nums):
            msf = max(msf ,x)

            if i == cand:
                cm = msf
            if x < cm - k:
                cand = i + 1
        return cand if cand < len(nums) else -1