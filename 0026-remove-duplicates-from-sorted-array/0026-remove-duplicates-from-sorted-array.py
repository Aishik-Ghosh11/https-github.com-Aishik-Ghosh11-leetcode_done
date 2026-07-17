class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        while left < len(nums) - 1:
            if nums[left] == nums[left + 1]:
                nums.pop(left)
            else:
                left += 1
        return len(nums)