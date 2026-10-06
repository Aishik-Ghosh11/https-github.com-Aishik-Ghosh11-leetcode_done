class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res = []
        n = len(nums)

        for i in nums:
            sp = [int(d) for d in str(i)]
            res.extend(sp)
        
        return res
