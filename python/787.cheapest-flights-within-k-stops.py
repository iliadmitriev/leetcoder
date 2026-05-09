class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        conn = defaultdict(list)
        for _from, _to, price, *_ in flights:
            conn[_from].append((_to, price))

        hq = [(0, k + 1, src)]
        vis = [0] * n
        vis[src] = 0

        while hq:
            total, stops, node = heapq.heappop(hq)

            if stops < 0:
                continue

            if vis[node] > stops:
                continue

            vis[node] = stops

            if node == dst:
                return total

            for child, price in conn[node]:
                heapq.heappush(hq, (total + price, stops - 1, child))
                

        return -1