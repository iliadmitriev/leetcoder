from typing import List


class Solution:
    def isArrangable(self, position: List[int], m: int, distance: int) -> bool:
        i = 0
        m -= 1

        for j in range(1, len(position)):

            if position[j] - position[i] >= distance:
                m -= 1
                i = j

            if m <= 0:
                break

        return m <= 0

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        # optimize
        if m == 2:
            return position[-1] - position[0]

        left, right = 1, (position[-1] - position[0]) // (m - 1)  # bessel's correction

        while left < right:
            mid = (left + right + 1) // 2
            if self.isArrangable(position, m, mid):
                left = mid
            else:
                right = mid - 1

        return left

