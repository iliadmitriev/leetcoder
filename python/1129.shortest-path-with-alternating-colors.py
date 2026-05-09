class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # build red and blue edges adjacency list
        # colors 0 - red, 1 - blue
        adj = [[[], []] for _ in range(n)]
        for u, v in redEdges:
            adj[u][0].append(v)
        for u, v in blueEdges:
            adj[u][1].append(v)
        # distances for red and blue paths from node 0
        distances = [[0, 0]] + [[inf, inf] for _ in range(n - 1)]
        # queue starts from 0-th node both red and blue edges
        queue = deque([(0, 0), (0, 1)])
        # start BFS
        while queue:
            node, color = queue.popleft()
            for neib in adj[node][1 - color]:
                if distances[neib][1 - color] == inf:
                    distances[neib][1 - color] = distances[node][color] + 1
                    queue.append((neib, 1 - color))
        return [dist if dist < inf else -1 for dist in map(min, distances)]