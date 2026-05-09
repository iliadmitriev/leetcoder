import heapq


class Solution:
    def leftmostBuildingQueries(
        self, heights: list[int], queries: list[list[int]]
    ) -> list[int]:
        ans = [-1] * len(queries)

        groups = [[] for _ in range(len(heights))]
        hq = []

        for i, (l, r) in enumerate(queries):
            l, r = min(l, r), max(l, r)
            bothHeight = max(heights[l], heights[r])

            if l == r or heights[l] < heights[r]:
                ans[i] = r
                continue

            groups[r].append((bothHeight, i))

        for i, height in enumerate(heights):

            for group in groups[i]:
                heapq.heappush(hq, group)

            while hq and hq[0][0] < height:
                _, idx = heapq.heappop(hq)
                ans[idx] = i

        return ans

