class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        count = 0
        queue = deque(u for u in range(numCourses) if in_degree[u] == 0)

        while queue:
            node = queue.popleft()
            count += 1

            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        return count == numCourses