class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def join(self, x: int, y: int) -> bool:
        par_x, par_y = self.find(x), self.find(y)

        if par_x == par_y:
            return False

        if self.rank[par_x] > self.rank[par_y]:
            self.parent[par_y] = par_x
            self.rank[par_x] += self.rank[par_y]
            self.rank[par_y] = 0
        else:
            self.parent[par_x] = par_y
            self.rank[par_y] += self.rank[par_x]
            self.rank[par_x] = 0

        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        queries_count, edges_count = len(queries), len(edgeList)
        answer = [False] * queries_count

        # sort edges(src, dst, dist) => sorted(dist, src, dst) - O(n log n)
        edges_list = sorted((l, s, d) for s, d, l in edgeList)
        # queries(s, d, l) => sorted(l, s, d, i) - O(n log n)
        indexed_queries = sorted((l, s, d, i) for i, (s, d, l) in enumerate(queries))
        curr_idx = 0
        # for current query limit, source, destination and index where to write result
        for limit, src, dest, idx in indexed_queries:
            # run trough algorithm and connect all the nodes with edges less than current limit
            while curr_idx < edges_count and edges_list[curr_idx][0] < limit:
                start, end = edges_list[curr_idx][1], edges_list[curr_idx][2]
                uf.join(start, end)
                curr_idx += 1

            answer[idx] = uf.connected(src, dest)

        return answer