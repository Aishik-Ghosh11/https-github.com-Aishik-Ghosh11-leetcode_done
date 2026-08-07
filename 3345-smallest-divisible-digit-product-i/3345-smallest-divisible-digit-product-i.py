class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # prod = 1
        while n:
            prod=1
            i=n
            while i:
                rem = i%10
                prod*=rem
                i//=10
            if prod%t == 0:
                return n
            else:
                n += 1
        return n