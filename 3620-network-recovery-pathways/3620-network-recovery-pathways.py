class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)


        def buildAdjacencyList() -> List[List[int]]:
            adj = [[] for _ in range(n)]
            for [u, v, cost] in edges:
                if online[u] and online[v]:
                    adj[u].append((v, cost))
            return adj
        
        def canReachNWithMinEdge(minEdge: int, adj: List[List[int]]) -> bool:
            cache = {}
            def dfs(node: int) -> int:
                if node in cache:
                    return cache[node]
                if node == n - 1:
                    return 0
                minVal = math.inf

                for [neighbor, cost] in adj[node]:
                    if cost < minEdge:
                        continue
                    val = dfs(neighbor)
                    if cost + val <= k:
                        minVal = min(minVal, cost + val)
                cache[node] = minVal
                return minVal
            
            return dfs(0) != math.inf
        
        adj = buildAdjacencyList()
        ans = -1
        lower = 0
        upper = 1e9

        while (lower <= upper):
            mid = (lower + upper) // 2
            if canReachNWithMinEdge(mid, adj):
                ans = mid
                lower = mid + 1
            else:
                upper = mid - 1
        
        return int(ans)




        