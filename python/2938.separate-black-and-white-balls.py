class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0

        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] == "0":
                i += 1

            while i < j and s[j] == "1":
                j -= 1

            swaps += j - i

            i, j = i + 1, j - 1

        return swaps

