class Solution:
    def countCommas(self, n: int) -> int:
        cnt , p = 0, 1000

        while p <= n:
            cnt += n - p + 1
            p *= 1000
        return cnt