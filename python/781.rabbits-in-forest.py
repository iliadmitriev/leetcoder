import math
from collections import Counter


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        freq = Counter(answers)
        total = 0

        for k, v in freq.items():
            total += (k + 1) * math.ceil(v / (k + 1))

        return total

