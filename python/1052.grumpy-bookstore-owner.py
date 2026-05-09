from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        satisfiedNotGrumpy = 0
        satisfiedGrumpy = 0
        maxSatisfiedGrumpy = 0

        for i in range(len(grumpy)):
            satisfiedNotGrumpy += customers[i] * (1 - grumpy[i])

            satisfiedGrumpy += customers[i] * grumpy[i]
            if i >= minutes:
                satisfiedGrumpy -= customers[i - minutes] * grumpy[i - minutes]
            maxSatisfiedGrumpy = max(maxSatisfiedGrumpy, satisfiedGrumpy)

        return satisfiedNotGrumpy + maxSatisfiedGrumpy

