class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for v in range(1, n):
            adj[parent[v]].append(v)

        sizes = [1] * n  # the node itself as a base value
        last = {}  # last[label] - the ancestor node of the same label

        def dfs(v: int) -> None:
            l = s[v]  # label of node v
            anc = last.get(l, -1)  # preserve the ancestor for a label

            last[l] = v  # set ancestor for a descendant nodes
            for u in adj[v]:
                dfs(u)

            last[l] = anc  # revert the ancestor for the label

            # drop the root (no parent)
            if v <= 0:
                return

            # append result to the ancestor of the same label or the parent
            p = anc if anc >= 0 else parent[v]
            sizes[p] += sizes[v]

        dfs(0)

        return sizes
