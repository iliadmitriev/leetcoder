class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [True] * n
        for _, to in edges:
            indegree[to] = False

        return [v for v in range(n) if indegree[v]]