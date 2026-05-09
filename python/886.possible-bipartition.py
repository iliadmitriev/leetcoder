from collections import deque, defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # build adjacency lists
        adj = defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        # graph colors: -1 - white, 1 - black, 0 - not colored yet
        colors = defaultdict(int)

        def find_colors(root: int) -> bool:
            """Find color for connected component."""
            colors[root] = 1
            queue = deque([root])
            while queue:
                node = queue.popleft()
                current_color = -colors[node]
                for new_node in adj[node]:
                    if new_node not in colors:
                        queue.append(new_node)
                        colors[new_node] = current_color
                    elif colors[new_node] == -current_color:
                        return False
            return True

        res = True
        for i in range(1, n + 1):
            if i not in colors:
                res = res and find_colors(i)
            if not res:
                return res
        return res