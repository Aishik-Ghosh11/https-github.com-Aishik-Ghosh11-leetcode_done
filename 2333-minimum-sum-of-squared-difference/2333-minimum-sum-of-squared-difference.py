class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        gaps = [abs(a - b) for a, b in zip(nums1, nums2)]

        def feasible(mid):
            return sum(max(gap - mid, 0) for gap in gaps) <= k

        l, r = 0, max(gaps)
        ans = r
        while l <= r:
            mid = (l + r) >> 1
            if feasible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        rest_k = k - sum(max(g - ans, 0) for g in gaps)
        gaps = [min(g, ans) for g in gaps]

        for i in range(len(gaps)):
            if rest_k == 0 or ans == 0:
                break
            if gaps[i] == ans:
                gaps[i] -= 1
                rest_k -= 1

        return sum(g * g for g in gaps)