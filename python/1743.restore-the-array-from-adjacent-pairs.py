class Solution:
    def dfs(selft, start, vis, adj):
        st = [start]
        res = []
        while st:
            node = st.pop()
            res.append(node)

            for child in adj[node]:
                if child in vis:
                    continue
                st.append(child)
                vis.add(child)
        return res

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # build adjacency lists
        n = len(adjacentPairs)
        adj = defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        
        # get random edge as start
        start1, start2 = adjacentPairs[0]
        vis = set([start1, start2])
        
        # dfs from first start and collect res1
        # dfs from second start and collect res2
        res1, res2 = self.dfs(start1, vis, adj), self.dfs(start2, vis, adj)

        return res2[::-1] + res1