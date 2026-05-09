class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for from_, to_, distance in roads:
            adj[from_].append((to_, distance))
            adj[to_].append((from_, distance))

        queue = deque([1])
        visited = set()
        visited.add(1)
        score = float("inf")
        while queue:
            node = queue.popleft()
            for next_, distance in adj[node]:
                score = min(score, distance)
                if next_ not in visited:
                    queue.append(next_)
                    visited.add(next_)
        return score