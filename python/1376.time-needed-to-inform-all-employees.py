from collections import deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for child, parent in enumerate(manager):
            if parent == -1:
                continue
            graph[parent].append(child)

        res = informTime[headID]
        queue = deque([(headID, informTime[headID])])
        while queue:
            parent, time = queue.popleft()
            res = max(res, time)

            for child in graph[parent]:
                queue.append((child, time + informTime[child]))

        return res