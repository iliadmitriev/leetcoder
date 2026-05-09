class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1.0 / value


        def dfs(path) -> float:
            start, end = path
            vis = set()
            stack = []
            if start in graph and end in graph :
                stack.append((start, 1.0))
                vis.add(start)

            while stack:
                node, value = stack.pop()

                if node == end:
                    return value

                for child, child_value in graph[node].items():
                    if child not in vis:
                        vis.add(child)
                        stack.append((child, value * child_value))
            return -1.0

        return list(map(dfs, queries))