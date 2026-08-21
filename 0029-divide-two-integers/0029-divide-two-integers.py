class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648 , 2147483647

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        is_negative = (dividend < 0) ^ (divisor < 0)

        dividend = -dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor

        quotient = 0

        while dividend <= divisor:
            power = 0
            while dividend <= (divisor << (power + 1)) and (divisor << (power + 1)) >= MIN_INT:
                power += 1

            quotient += (1 << power)
            dividend -= (divisor << power)
        
        return -quotient if is_negative else quotient






















