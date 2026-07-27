class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lst = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                lst.append((nums[i]-1)*(nums[j]-1))
        return max(lst)