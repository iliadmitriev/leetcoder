class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:
        n = len(mountain)
        peaks: list[int] = []
        for i in range(1, n - 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                peaks.append(i)

        return peaks

