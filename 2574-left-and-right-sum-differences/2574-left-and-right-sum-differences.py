class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls = []
        rs = []

        for i in range(len(nums)):
            a = sum(nums[:i])
            b = sum(nums[i+1:])
            ls.append(a)
            rs.append(b)

        z = []
        for i in range(len(nums)):
            z.append(abs(ls[i] - rs[i]))
        
        return z










