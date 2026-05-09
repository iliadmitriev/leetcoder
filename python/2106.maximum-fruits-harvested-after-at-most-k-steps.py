import bisect


class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        return self.maxTotalFruits_v2(fruits, startPos, k)

    def maxTotalFruits_v2(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        def stepsCount(fruits, startPos, left, right):
            rightPart = fruits[right][0] - startPos
            leftPart = startPos - fruits[left][0]
            bothParts = rightPart + leftPart

            if startPos <= fruits[left][0]:
                return rightPart
            elif startPos >= fruits[right][0]:
                return leftPart

            return min(leftPart, rightPart) + bothParts

        n = len(fruits)

        left = 0
        cur = 0
        maxFruits = 0

        for right in range(n):
            cur += fruits[right][1]

            while left <= right and stepsCount(fruits, startPos, left, right) > k:
                cur -= fruits[left][1]
                left += 1

            maxFruits = max(maxFruits, cur)

        return maxFruits

    def maxTotalFruits_v1(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        prefix = [0] * (n + 1)
        positions = [0] * n
        for i, (pos, count) in enumerate(fruits):
            prefix[i + 1] = prefix[i] + count
            positions[i] = pos

        maxCur = 0

        for x in range(k // 2 + 1):
            # move x steps to the left and then turn right,
            # move back to start and move the rest of the steps
            left = startPos - x
            right = startPos + k - 2 * x
            start = bisect.bisect_left(positions, left)
            end = bisect.bisect_right(positions, right)

            maxCur = max(maxCur, prefix[end] - prefix[start])

            # move x steps to the right and then turn left,
            # move back to start and move the rest of the steps
            right = startPos + x
            left = startPos - k + 2 * x
            start = bisect.bisect_left(positions, left)
            end = bisect.bisect_right(positions, right)

            maxCur = max(maxCur, prefix[end] - prefix[start])

        return maxCur

