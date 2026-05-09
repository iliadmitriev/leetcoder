class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        a, b = 0, 0
        prev = "#"
        count = 0

        for v in s:
            if v == prev:
                a += 1
            else:
                count += min(a, b)
                a, b = 1, a

            prev = v

        count += min(a, b)

        return count

