class Solution:
    def checkDivisibility(self, n: int) -> bool:

        def digitSum(val):
            s=0
            while val:
                r = val % 10
                s += r
                val //= 10

            return s
        
        def digitprod(val):
            p=1
            while val:
                r = val%10
                p *= r
                val //= 10
            
            return p
        
        s = digitprod(n) + digitSum(n)
        if n%s==0:
            return True
        return False

