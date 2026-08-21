import math

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        
        def count(x: int) -> int:
            cnt = 0
            for mask in range(1, 1 << n):
                lcm_val = 1
                bits = 0
                for i in range(n):
                    if (mask >> i) & 1:
                        bits += 1
                        lcm_val = math.lcm(lcm_val, coins[i])
                        if lcm_val > x:
                            break
                if lcm_val <= x:
                    if bits % 2 == 1:
                        cnt += x // lcm_val
                    else:
                        cnt -= x // lcm_val
            return cnt

        low = 1
        high = min(coins) * k

        ans = high
        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


























        