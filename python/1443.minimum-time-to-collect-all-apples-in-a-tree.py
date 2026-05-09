class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # (node, visited, parent node)
        stack = [(0, False, None)]
        res = 0
        cache = defaultdict(int)
        while stack:
            node, vis, parent = stack.pop()
            if vis:
                if node and hasApple[node] or cache[node]:
                    res += 2
                    if parent:
                        cache[parent] = True
            else:
                stack.append((node, True, parent))
                for child in reversed(adj[node]):
                    if child != parent:
                        stack.append((child, False, node))

        return res
