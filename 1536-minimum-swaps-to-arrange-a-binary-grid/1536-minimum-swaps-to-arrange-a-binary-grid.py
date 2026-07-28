class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxRight = []
        for i in range(n):
            last_idx = 0
            for j in range(n):
                if grid[i][j]:
                    last_idx = j
            maxRight.append(last_idx)
        print(maxRight)
        swaps = 0
        for i in range(n):
            required = i
            if maxRight[i] <= required:
                continue
            
            found = False
            for j in range(i+1, n):
                if maxRight[j] <= required:
                    found = True
                    break
            
            if not found:
                return -1

            for k in range(j, i, -1):
                maxRight[k], maxRight[k-1] = maxRight[k-1], maxRight[k]
                swaps += 1
        
        return swaps