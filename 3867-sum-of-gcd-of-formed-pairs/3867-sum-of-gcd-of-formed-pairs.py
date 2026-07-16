class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        prefixGcd = [0] * len(nums)
        max_ele = -1
        for i in range(len(nums)):
            max_ele = max(nums[i], max_ele)
            prefixGcd[i] = gcd(nums[i], max_ele)
        
        sortedPrefixGcd = sorted(prefixGcd)

        l = 0
        r = len(sortedPrefixGcd) - 1

        res = 0
        while (l < r):
            res += gcd(sortedPrefixGcd[l], sortedPrefixGcd[r])
            l += 1
            r -= 1
        
        return res
