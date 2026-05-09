class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        res = -1
        vis = [False] * n
        for start_node in range(n):
            if not vis[start_node]:
                vis[start_node] = True
                queue = deque([start_node])
                idx = {start_node: 0}
                while queue:
                    node = queue.popleft()
                    next_ = edges[node]

                    if next_ == -1:
                        continue

                    if not vis[next_]:
                        idx[next_] = idx[node] + 1
                        queue.append(next_)
                        vis[next_] = True
                        
                    elif vis[next_] and node in idx and next_ in idx:
                        res = max(res, idx[node] + 1 - idx[next_])

        return res
