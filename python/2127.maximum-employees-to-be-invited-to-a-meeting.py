from collections import deque


class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        N = len(favorite)
        depth = [1] * N
        inDegree = [0] * N

        for node in range(N):
            inDegree[favorite[node]] += 1

        q = deque([n for n in range(N) if inDegree[n] == 0])
        while q:
            node = q.popleft()
            nnode = favorite[node]

            depth[nnode] = max(depth[nnode], depth[node] + 1)

            inDegree[nnode] -= 1
            if inDegree[nnode] == 0:
                q.append(nnode)

        longestCycle = 0
        longestTwoNodePath = 0

        for node in range(N):
            if inDegree[node] == 0:
                continue

            cycleLen = 0
            cur = node
            while inDegree[cur] != 0:
                inDegree[cur] = 0
                cur = favorite[cur]
                cycleLen += 1

            if cycleLen == 2:
                longestTwoNodePath += depth[node] + depth[favorite[node]]
            else:
                longestCycle = max(longestCycle, cycleLen)

        return max(longestCycle, longestTwoNodePath)

