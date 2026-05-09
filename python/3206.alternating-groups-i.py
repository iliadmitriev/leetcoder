class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        count = 0
        n = len(colors)

        for i in range(len(colors)):
            if colors[(i - 1) % n] != colors[i] != colors[(i + 1) % n]:
                count += 1

        return count

