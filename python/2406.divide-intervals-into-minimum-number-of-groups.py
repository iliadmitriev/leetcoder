class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        inv: list[tuple[int, int]] = []
        for start, end in intervals:
            inv.append((start, 1))
            inv.append((end + 1, -1))

        inv.sort()

        curGroups, maxGroups = 0, 0
        for _, group in inv:
            curGroups += group
            maxGroups = max(maxGroups, curGroups)

        return maxGroups

