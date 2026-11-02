class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        DIR = [(1,0),(0,1)]
        MOD = 10 ** 9 + 7
        
        prev = [[0] * 2 for _ in range(N + 1)]
        curr = [[0] * 2 for _ in range(N + 1)]
        
        curr[N - 1] = [1] * 2 # base case
        
        for x in reversed(range(M)):
            for y in reversed(range(N)):
                if x == M - 1 and y == N - 1: continue
                
                for prevDir in range(2):
                    if grid[x][y]:
                        # is mirror
                        dir = not prevDir
                        dx, dy = DIR[dir]
                        i, j = x + dx, y + dy
                        
                        curr[y][prevDir] = curr[j][dir] if i == x else prev[j][dir]
                    else:
                        # is not a mirror
                        res = 0
            
                        for dir, (dx, dy) in enumerate(DIR):
                            i, j = x + dx, y + dy
                            
                            res += curr[j][dir] if i == x else prev[j][dir]

                        curr[y][prevDir] = res % MOD
                
            prev, curr = curr, prev
        
        return prev[0][0]