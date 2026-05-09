import collections


class Solution:
    def maxCandies(
        self,
        status: list[int],
        candies: list[int],
        keys: list[list[int]],
        containedBoxes: list[list[int]],
        initialBoxes: list[int],
    ) -> int:
        total = 0
        q = collections.deque()

        # status:
        # 0: locked, not visited
        # 1: unlocked, not visited
        # -1: locked, visited
        # -2: unlocked, visited (final)

        for box in initialBoxes:
            if status[box] == 1:
                q.append(box)
                status[box] = -2
            else:
                status[box] = -1

        while q:
            box = q.popleft()
            total += candies[box]

            for key in keys[box]:
                if status[key] == -1:
                    q.append(key)
                status[key] = 1

            for nextBox in containedBoxes[box]:
                if status[nextBox] == 1:
                    q.append(nextBox)
                    status[box] = -2
                elif status[nextBox] == 0:
                    status[nextBox] = -1

        return total

