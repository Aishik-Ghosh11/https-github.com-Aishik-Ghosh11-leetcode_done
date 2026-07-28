class Solution:
    def maximumProduct(self, A: List[int]) -> int:
        A.sort()      
        n = len(A)  
        return max(
            A[-1] * A[-2] * A[-3],
            A[-1] * A[0] * A[1]
        )