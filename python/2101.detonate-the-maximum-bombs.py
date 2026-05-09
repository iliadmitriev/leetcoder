from collections import defaultdict, deque


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        # I - build directed graph respecting distance
        graph = defaultdict(list)
        indegree = [0] * n
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if i != j and r1 ** 2 >= (x2 - x1) ** 2 + (y2 - y1) ** 2:
                    graph[i].append(j)
                    indegree[j] += 1
                    # optimizatio 1: if there is fully connected vertex
                    # all vertices could be reached from it (return all vertices count)
                    if len(graph[i]) == n - 1:
                        return n

        vertices = sorted(range(n), key=indegree.__getitem__)
        
        def bfs(start: int) -> int:
            vis = {start}
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in vis:
                        queue.append(v)
                        vis.add(v)
            return len(vis)
            

        count = 0
        for v in vertices:
            count = max(count, bfs(v))
            # optimization 2: if there is vertex that all vertices can be reached from:
            # all vertices could be reached if start from it (return all vertices count)
            # no need to find another solution (it's maximum)
            if count == n:
                break

        return count