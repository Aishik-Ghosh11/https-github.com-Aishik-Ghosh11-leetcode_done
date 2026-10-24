class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = (1 << max(nums).bit_length()) - 1
        for i, v in enumerate(nums):
            if i != v:
                while v != i:
                    res = res & v
                    nums[v], nums[i] = nums[i], nums[v]
                    v = nums[i]
                    res = res & v
        
        return res if res != len(nums)-1 else 0
        
