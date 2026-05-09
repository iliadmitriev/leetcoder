import heapq


class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        n, m = len(nums), len(queries)
        diff = [0] * (n + 1)  # query cumulative value
        cur = 0  # current prefix sum
        hq = []  # max heap for storing right bounds
        j = 0  # current query index

        queries.sort(key=lambda x: (x[0], -x[1]))

        for i, num in enumerate(nums):
            cur += diff[i]

            # push all right bounds to max heap with the same left bound
            while j < m and queries[j][0] == i:
                heapq.heappush(hq, -queries[j][1])
                j += 1

            # try to get current value greater or equal to current num, to make it 0
            # and add right bounds to diff
            while cur < num and hq and -hq[0] >= i:
                cur += 1
                diff[-heapq.heappop(hq) + 1] -= 1

            if cur < num:
                return -1

        return len(hq)

