class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(start):
            if start == len(nums) -1:
                if nums not in res:
                    res.append(nums[:])
                return
            
            for n in range(start, len(nums)):
                nums[start], nums[n] = nums[n], nums[start]
                backtrack(start+1)
                nums[start], nums[n] = nums[n], nums[start]
        
        backtrack(0)
        return res