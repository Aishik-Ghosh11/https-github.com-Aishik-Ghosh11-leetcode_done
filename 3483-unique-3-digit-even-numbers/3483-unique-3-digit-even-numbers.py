from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:    
        avail = Counter(digits)
        count = 0
        for num in range(100, 1000, 2):
            d1, d2, d3 = num // 100, (num // 10) % 10, num % 10
            need = Counter([d1, d2 ,d3])
            if all(avail[d] >= c for d, c in need.items()):
                count += 1
        return count
