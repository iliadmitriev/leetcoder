

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)
        A, B = tops[0], bottoms[0]

        for a, b in zip(tops, bottoms):
            if A != a and A != b:
                A = 0
            if B != a and B != b:
                B = 0

            if not A and not B:
                return -1

        mostFreq = A or B

        return min(n - tops.count(mostFreq), n - bottoms.count(mostFreq))

