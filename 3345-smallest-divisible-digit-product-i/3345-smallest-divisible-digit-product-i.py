class Solution:
    def findDigitsProd(self, n: int) -> int:
        prod = 1
        while n:
            prod = prod * (n % 10)
            # Early exit if product found the 0 
            if prod == 0:
                return 0
            n //= 10
        return prod

    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n, n+10):
            if self.findDigitsProd(num) % t == 0:
                return num

        return-1
