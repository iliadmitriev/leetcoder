class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        n = len(s)

        for i, ch in enumerate(s):
            idx = ord(ch) - ord("a")
            posRight = i + distance[idx] + 1
            posLeft = i - distance[idx] - 1

            if (posRight < n and s[posRight] == ch) or (
                posLeft >= 0 and s[posLeft] == ch
            ):
                continue

            return False

        return True

