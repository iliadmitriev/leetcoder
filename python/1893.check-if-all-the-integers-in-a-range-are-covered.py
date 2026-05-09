class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:

        cover = [0] * 52
        for start, end in ranges:
            cover[start] += 1
            cover[end + 1] -= 1

        coverage = 0
        for curr in range(1, right + 1):
            coverage += cover[curr]

            if left <= curr and coverage == 0:
                return False

        return True

