from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def man_dist(p1,p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        safeness = [[0 for _ in range(n)] for i in range(n)]
        dirs = [(1,0),(-1,0), (0,1), (0,-1)]
        def isFeasible(x,y):
            return 0<=x<=n-1 and 0<=y<=n-1 
        seen = set()
        queue = deque()
        for i in range(n): # (n^2)
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j,0))
                    seen.add((i,j))
                    safeness[i][j] = 0
        while queue: # this costs (n^2)
            x, y, dist = queue.popleft()
            for dx, dy in dirs:
                x2 = x + dx
                y2 = y + dy
                if isFeasible(x2,y2) and (x2,y2) not in seen:
                    seen.add((x2,y2))
                    safeness[x2][y2] = dist + 1
                    queue.append((x2,y2,dist+1))

        # let's do djikstra

        sources = {(0,0): safeness[0][0]}
        heap = [(-safeness[0][0],0,0)]    
        heapq.heapify(heap)

        while heap:
            dist, x, y = heapq.heappop(heap)
            dist = -dist
            if dist < sources[(x,y)]:
                continue
            for dx,dy in dirs:
                x2 = x + dx
                y2 = y + dy
                if isFeasible(x2,y2):
                    d_new = min(dist, safeness[x2][y2])
                    if d_new > sources.get((x2,y2), float("-inf")):
                        sources[(x2,y2)] = d_new
                        heapq.heappush(heap,(-d_new,x2,y2))
        
        return sources[(n-1,n-1)]
        
        
        
            
        