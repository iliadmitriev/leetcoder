from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        weights = [0] * (max(people) + 1)
        for person in people:
            weights[person] += 1

        left, right = 0, len(weights) - 1

        while left <= right:

            while left <= right and weights[left] <= 0:
                left += 1

            while left <= right and weights[right] <= 0:
                right -= 1

            if left > right:
                break

            if left + right <= limit:
                weights[left] -= 1

            weights[right] -= 1

            boats += 1

        return boats

