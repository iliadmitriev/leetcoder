class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        alternating = 0
        curAlt = 1

        for i in range(1, n + k - 1):
            if colors[(i - 1) % n] == colors[i % n]:
                curAlt = 1
                continue

            curAlt += 1
            if curAlt >= k:
                alternating += 1

        return alternating

