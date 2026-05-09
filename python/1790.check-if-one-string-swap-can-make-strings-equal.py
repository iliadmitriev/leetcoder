class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        swaps = 2
        ind = -1

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue

            swaps -= 1

            if swaps < 0:
                return False

            if ind >= 0:
                if s1[ind] != s2[i] or s1[i] != s2[ind]:
                    return False

            if ind == -1:
                ind = i

        return swaps in [0, 2]

