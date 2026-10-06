class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            s = str(num)
            for ch in s:
                res.append(int(ch))
        
        return res
