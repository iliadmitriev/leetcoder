class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        secrets = set([0, firstPerson])
        # adjacency list for unordered graph time -> from -> to
        time_map = defaultdict(lambda: defaultdict(list))

        for src, dst, t in meetings:
            time_map[t][src].append(dst)
            time_map[t][dst].append(src)

        def dfs(src, adj, vis):
            if src in vis:
                return

            vis.add(src)
            secrets.add(src)

            for child in adj[src]:
                dfs(child, adj, vis)

        for t in sorted(time_map.keys()):
            visited = set()
            for src in time_map[t]:
                if src in secrets:
                    dfs(src, time_map[t], visited)

        return list(secrets)

