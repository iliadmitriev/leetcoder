from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        colors = [None] * n

        def bfs(start: int) -> bool:
            queue = deque([start])
            colors[start] = 0
            while queue:
                node = queue.popleft()
                for child in graph[node]:
                    if colors[child] is None:
                        colors[child] = 1 - colors[node]
                        queue.append(child)
                    elif colors[child] != 1 - colors[node]:
                        return False
            return True


        for start in range(n):
            if colors[start] is None and not bfs(start):
                return False
        return True
            

            