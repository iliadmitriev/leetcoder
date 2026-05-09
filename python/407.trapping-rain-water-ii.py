import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        NROWS, NCOLS = len(heightMap), len(heightMap[0])
        res = 0
        maxHeight = 0
        minHeap = []
        vis = [[False] * NCOLS for _ in range(NROWS)]

        for i in range(NROWS):
            minHeap.append((heightMap[i][0], i, 0))
            minHeap.append((heightMap[i][NCOLS - 1], i, NCOLS - 1))
            vis[i][0] = vis[i][NCOLS - 1] = True

        for j in range(1, NCOLS - 1):
            minHeap.append((heightMap[0][j], 0, j))
            minHeap.append((heightMap[NROWS - 1][j], NROWS - 1, j))
            vis[0][j] = vis[NROWS - 1][j] = True

        heapq.heapify(minHeap)

        while minHeap:
            height, r, c = heapq.heappop(minHeap)
            maxHeight = max(maxHeight, height)
            res += maxHeight - height

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if nr < 0 or nr == NROWS or nc < 0 or nc == NCOLS:
                    continue

                if vis[nr][nc]:
                    continue

                vis[nr][nc] = True
                heapq.heappush(minHeap, (heightMap[nr][nc], nr, nc))

        return res

