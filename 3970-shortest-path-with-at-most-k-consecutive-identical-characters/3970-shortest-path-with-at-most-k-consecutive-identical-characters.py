from queue import PriorityQueue

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, wt in edges:
            adj[u].append((v, wt))

        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        dist[0][1] = 0

        q = PriorityQueue()
        q.put((0, 0, 1))  # cost, node, curr_k

        while not q.empty():
            cost, node, curr_k = q.get()

            if cost != dist[node][curr_k]:
                continue

            if node == n - 1:
                return cost

            for new_node, wt in adj[node]:

                if labels[new_node] == labels[node]:
                    new_k = curr_k + 1
                else:
                    new_k = 1

                if new_k > k:
                    continue

                new_cost = cost + wt

                if new_cost < dist[new_node][new_k]:
                    dist[new_node][new_k] = new_cost
                    q.put((new_cost, new_node, new_k))

        return -1









































