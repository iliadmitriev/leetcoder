from collections import defaultdict
from typing import List


class Solution:
    def maximumScoreAfterOperations(
        self, edges: List[List[int]], values: List[int]
    ) -> int:

        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(cur: int, prev: int) -> int:
            if len(adj[cur]) == 1 and prev != -1:
                return values[cur]

            child_sum = 0
            for child in adj[cur]:
                if child == prev:
                    continue

                child_sum += dfs(child, cur)

            return min(child_sum, values[cur])

        return sum(values) - dfs(0, -1)

