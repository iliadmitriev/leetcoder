

class Solution:
    @staticmethod
    def searchMaxByEnd(arr: list[list[int]], x: int) -> int:
        lo, hi = 0, len(arr)

        while lo < hi:
            mid = (lo + hi) // 2

            if arr[mid][0] < x:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def maxTwoEvents(self, events: list[list[int]]) -> int:
        maxSum = 0

        events.sort()
        n = len(events)
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = max(suffix[i + 1], events[i][2])

        for _, b, value in events:
            nextIdx = self.searchMaxByEnd(events, b + 1)
            maxSum = max(maxSum, value + suffix[nextIdx])

        return maxSum


