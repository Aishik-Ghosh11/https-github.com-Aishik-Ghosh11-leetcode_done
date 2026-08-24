class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if target > nums[i]:
                continue
            if target < nums[i]:
                return i
        else:
            if target > nums[len(nums)-1]:
                return len(nums)