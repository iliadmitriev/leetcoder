
from collections import deque


class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:

        n = len(parents)

        adj: list[list[int]] = [[] for _ in range(n)]
        child: list[int] = [1] * n
        inorder: list[int] = [0] * n

        for i, p in enumerate(parents):
            if p == -1:
                continue
            adj[p].append(i)
            inorder[p] += 1

        q = deque([i for i in range(n) if inorder[i] == 0])
        while q:
            ch = q.popleft()
            par = parents[ch]
            if par == -1:
                continue

            inorder[par] -= 1
            child[par] += child[ch]
            if inorder[par] == 0:
                q.append(par)

        # def dfsCountChild(i: int) -> int:
        #     child[i] = 1
        #     for j in adj[i]:
        #         child[i] += dfsCountChild(j)
        #     return child[i]

        maxScore = 0
        count = 0
        for i in range(n):
            val = max(1, n - child[i])

            for j in adj[i]:
                val *= child[j]

            if val > maxScore:
                count = 1
                maxScore = val
            elif val == maxScore:
                count += 1

        return count

