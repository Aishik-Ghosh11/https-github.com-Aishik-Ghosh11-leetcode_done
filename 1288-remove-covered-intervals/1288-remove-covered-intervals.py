class Solution:
    def removeCoveredIntervals(self, A: list[list[int]]) -> int:
        remain = len(A)
        A.sort(key=lambda x: (x[0], -x[1]))
        for i in range(len(A)):
            for j in range(len(A)):
                if i == j:
                    continue
                if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
                    remain -= 1
                    break
        
        return remain

