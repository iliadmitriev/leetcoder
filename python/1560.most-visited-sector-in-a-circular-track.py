class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        start = rounds[0]
        end = rounds[-1]

        if start > end:
            return list(range(1, end + 1)) + list(range(start, n + 1))

        return list(range(start, end + 1))

