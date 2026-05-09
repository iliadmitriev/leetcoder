class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        maxCounter = 0

        for bit in range(24):
            mask = 1 << bit
            counter = 0

            for num in candidates:
                if num & mask:
                    counter += 1

            maxCounter = max(maxCounter, counter)

        return maxCounter

