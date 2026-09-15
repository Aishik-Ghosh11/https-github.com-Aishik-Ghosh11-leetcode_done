class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        def helper(nums):
            ans = [0] * len(nums)
            sums = collections.defaultdict(int)
            counts = collections.defaultdict(int)
            for i, x in enumerate(nums):
                ans[i] += i * counts[x] - sums[x]
                sums[x] += i
                counts[x] += 1
            return ans
        
        left = helper(nums)
        right = helper(nums[::-1])
        return [x + y for x, y in zip(left , right[::-1])]