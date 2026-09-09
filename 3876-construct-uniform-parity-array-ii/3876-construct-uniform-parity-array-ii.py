class Solution:
    def uniformArray(self, A: list[int]) -> bool:
        A.sort()
        n = len(A)
        x = A[0]
        if x % 2 == 0:
            parity = 'even'
        else:
            parity = 'odd'
        for i in range(1, n):
            t = A[i]
            if t % 2 == 0:
                p = 'evev'
            else: 
                p = 'odd'
            
            if parity != p:
                s = abs(t - x)
                if s % 2 == 0:
                    p = 'even'
                else: p = 'odd'

                if parity != p:
                    return False
        return True