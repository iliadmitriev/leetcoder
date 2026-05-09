from collections import defaultdict, deque


class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        maxColors = 0
        n = len(colors)
        visited = 0
        invAdj = [[] for _ in range(n)]
        indegree = [0] * n
        colorsCount = [defaultdict(int) for _ in range(n)]

        for src, dst in edges:
            invAdj[dst].append(src)
            indegree[src] += 1

        queue = deque([i for i in range(n) if indegree[i] == 0])

        while queue:
            node = queue.popleft()
            visited += 1
            colorsCount[node][colors[node]] += 1
            maxColors = max(maxColors, colorsCount[node][colors[node]])

            for child in invAdj[node]:
                for col in colorsCount[node].keys():
                    colorsCount[child][col] = max(
                        colorsCount[child][col], colorsCount[node][col]
                    )

                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        if visited < n:
            return -1

        return maxColors

