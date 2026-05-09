

class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: list[int], endTime: list[int]
    ) -> int:
        n = len(startTime)
        spaces = []

        prev = 0
        for start, end in zip(startTime, endTime):
            spaces.append(start - prev)
            prev = end

        spaces.append(eventTime - prev)

        # get indexes of the 3 biggest spaces
        a, b, c = -1, -1, -1
        for i in range(n + 1):
            if a < 0 or spaces[i] > spaces[a]:
                c, b, a = b, a, i
            elif b < 0 or spaces[i] > spaces[b]:
                c, b = b, i
            elif c < 0 or spaces[i] > spaces[c]:
                c = i

        maxFreeSpace = 0

        for i in range(n):
            mid = endTime[i] - startTime[i]
            left, right = spaces[i], spaces[i + 1]

            maxFreeSpace = max(maxFreeSpace, left + right)

            # if there is free space to move the meeting between gaps somewhere else
            # check if one of spaces a, b or c is not occupied, and current meeting is fit there
            if (
                (i != a and i + 1 != a and mid <= spaces[a])
                or (i != b and i + 1 != b and mid <= spaces[b])
                or (i != c and i + 1 != c and mid <= spaces[c])
            ):
                maxFreeSpace = max(maxFreeSpace, left + mid + right)

        return maxFreeSpace

