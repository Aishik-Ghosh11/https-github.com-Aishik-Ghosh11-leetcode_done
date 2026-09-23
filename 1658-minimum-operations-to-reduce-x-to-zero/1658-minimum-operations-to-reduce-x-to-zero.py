class Solution:
    def minOperations(self, A: list[int], x: int) -> int:
        n = len(A)
        target = sum(A) - x

        if target < 0:
            return -1
        
        start = end = 0
        res = -1

        total = 0

        while end < n:
            total += A[end]

            while total > target:
                total -= A[start]
                start += 1
            
            if total == target:
                res = max(res, end - start + 1)
            
            end += 1
        
        if res == -1:
            return -1
        
        return n-res
        





























