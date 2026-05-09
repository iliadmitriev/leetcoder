from heapq import heappush, heappop


def dist(p1: list[int, int], p2: list[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # number of vertices
        n = len(points)
        # weight, vertice #
        hq = [(0, 0)]
        # all visited vertices
        seen = [False] * n

        # result 
        mst = 0
        count = 0

        while count < n:
            weight, point_idx = heappop(hq)

            if seen[point_idx]:
                continue

            seen[point_idx] = True
            mst += weight
            count += 1

            for next_idx in range(n):
                if not seen[next_idx]:
                    heappush(
                        hq, (dist(points[point_idx], points[next_idx]), next_idx)
                    )
        
        return mst






