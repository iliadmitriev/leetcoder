class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: list[int], endTime: list[int]
    ) -> int:
        spaces = []  # list of spaces lengths
        maxFree = 0

        prev = 0
        for start, end in zip(startTime, endTime):
            if start >= prev:
                spaces.append(start - prev)
            prev = end

        if eventTime >= prev:
            spaces.append(eventTime - prev)

        curFree = 0

        for right in range(len(spaces)):
            curFree += spaces[right]

            left = right - k - 1
            if left >= 0:
                curFree -= spaces[left]

            maxFree = max(maxFree, curFree)

        return maxFree

