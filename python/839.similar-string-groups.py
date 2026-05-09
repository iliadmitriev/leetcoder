def check_similar(s1: str, s2: str):
    if s1 == s2:
        return True
    ct = 0
    for i, j in zip(s1, s2):
        if i != j:
            if ct == 2:
                return False
            ct += 1
    
    return True


def bfs(vis: set, start: int, graph):
    vis.add(start)
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for next_ in graph[node]:
            if next_ not in vis:
                vis.add(next_)
                queue.append(next_)


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        n = len(strs)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if check_similar(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        components = 0
        vis = set()
        for start in range(n):
            if start not in vis:
                components += 1
                bfs(vis, start, graph)

        return components
