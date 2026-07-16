class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = sum(nums[:3])
        nums = sorted(nums)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if abs(nums[i] + nums[j] + nums[k] - target) < abs(ans - target):
                    ans = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] < target:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                else:
                    return target
        
        return ans