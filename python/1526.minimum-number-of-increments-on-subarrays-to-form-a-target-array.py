class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        total = 0
        prev = 0

        for num in target:
            if num > prev:
                total += num - prev

            prev = num

        return total

