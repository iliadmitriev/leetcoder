class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        stack = [(0, None, False)]
        cache = {}
        res = [0] * n
        while stack:
            node, parent, process = stack.pop()
            if process:
                counter = cache.pop(node)
                res[node] = counter[labels[node]]
                if parent in cache:
                    cache[parent] += counter
            else:
                stack.append((node, parent, True))
                cache[node] = Counter()
                cache[node][labels[node]] += 1
                for nei in reversed(tree[node]):
                    if parent != nei:
                        stack.append((nei, node, False))
        return res