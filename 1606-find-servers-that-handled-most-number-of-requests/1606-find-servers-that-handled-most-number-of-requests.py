class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        """
        Time Complexity: O(n log k)
        Space Complexity: O(n)
        """
        arrival.append(float('inf'))
        load.append(0)

        max_requests_served = 0
        requests_served = [0] * k
        idle_servers = [i for i in range(k)]
        working_servers = []

        for i, (arrival_time, cost) in enumerate(zip(arrival, load)):
            # If working servers time is leq than current time we set it back to idle
            while working_servers and working_servers[0][0] <= arrival_time:
                _, idx = heapq.heappop(working_servers)
                heapq.heappush(idle_servers, i + (idx - i) % k)

            # Process the time
            if arrival_time != float('inf') and idle_servers:
                current_server = heapq.heappop(idle_servers)
                requests_served[current_server % k] += 1
                heapq.heappush(working_servers, (arrival_time + cost, current_server))
        max_requests_served = max(requests_served)
        return [i for i, cts in enumerate(requests_served) if cts == max_requests_served]