from typing import List
from functools import cache

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            nums[i] %= k

        @cache
        def go(index, remainder):
            if index == n:
                current = [0] * k
                current[remainder] += 1
                return current

            # Mantém o resto sempre entre 0 e k - 1
            new_remainder = (remainder * nums[index]) % k

            further = go(index + 1, new_remainder)

            current = further[:]
            current[remainder] += 1

            return current

        total = [0] * k

        for i in range(n):
            further = go(i + 1, nums[i])

            for j in range(k):
                total[j] += further[j]

        return total