class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)

        # BFS from k
        suspicious = set()
        q = deque([k])
        suspicious.add(k)

        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    q.append(neighbor)

        for a, b in invocations: 
            if a not in suspicious and b in suspicious:
                return list(range(n))


        return [i for i in range(n) if i not in suspicious]
        
        