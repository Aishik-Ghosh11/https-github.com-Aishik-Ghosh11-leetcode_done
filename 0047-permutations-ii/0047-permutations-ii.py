class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        for val in permutations(nums):
            if val not in res:
                res.append(val)
        
        return res
