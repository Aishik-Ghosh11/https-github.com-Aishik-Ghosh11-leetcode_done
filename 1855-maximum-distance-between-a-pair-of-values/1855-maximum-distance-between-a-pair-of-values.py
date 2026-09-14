class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n1, n2 = len(nums1), len(nums2)
        for i in range(n1):
            l, r = 0, n2-1
            while l < r:
                mid = (l+r+1)//2
                if nums2[mid] >= nums1[i]:
                    l = mid
                else:
                    r = mid-1
            ans = max(ans, l-i)
        return ans