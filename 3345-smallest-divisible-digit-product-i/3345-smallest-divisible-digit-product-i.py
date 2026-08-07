class Solution:
    def findDigitsProd(self, num: int) -> int:
        prod = 1
        while num > 0:
            prod = prod * (num % 10)
            # Early exit if product hits 0
            if prod == 0:
                return 0
            num //= 10 
        
        return prod 
        
    def smallestNumber(self, n: int, t: int) -> int:

        for num in range(n, n + 10):
            if self.findDigitsProd(num) % t == 0:
                return num

        return -1