class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for a, b, w in times:
            adj[a].append((b, w))
            
        queue = [(0, k)]
        ping = { x:float("inf") for x in range(1, n + 1) }
        ping[k] = 0
        
        while queue:
            reach, node = heapq.heappop(queue)
            
            if ping[node] < reach:
                continue
            
            for neighobour, w in adj[node]:
                if ping[neighobour] > w + reach:
                    ping[neighobour] = w + reach
                    heapq.heappush(queue, (w + reach, neighobour))
                    
        res = max(ping.values())
        return res if res != float("inf") else -1
    