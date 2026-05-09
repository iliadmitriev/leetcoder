class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        stack = [(0, False)]
        path = []
        res = []

        while stack:
            node, vis = stack.pop()

            if vis:
                if node == target:
                    res.append(path.copy())
                path.pop(-1)
            else:
                path.append(node)
                stack.append((node, True))
                for nei in reversed(graph[node]):
                    stack.append((nei, False))
        return res
