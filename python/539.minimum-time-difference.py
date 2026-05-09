class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:

        day = 24 * 60

        times = sorted([int(t[:2]) * 60 + int(t[3:]) for t in timePoints])
        minDiff = day
        for i in range(1, len(times)):
            minDiff = min(minDiff, times[i] - times[i - 1])

        return min(minDiff, (day + times[0] - times[-1]) % day)

