from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        totalMaxImportance = 0

        inDegree = [0] * n

        for u, v in roads:
            inDegree[u] += 1
            inDegree[v] += 1

        vertices = list(range(n))
        vertices.sort(key=lambda x: inDegree[x])
        importance = [0] * n
        for i, v in enumerate(vertices):
            importance[v] = i + 1

        for u, v in roads:
            totalMaxImportance += importance[u] + importance[v]
        return totalMaxImportance

