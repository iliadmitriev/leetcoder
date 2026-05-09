class Solution:
    def countSegments(self, s: str) -> int:
        seg = 0
        prev = " "

        # count number of transitions from space to non-space
        for c in s:
            if c != " " and prev == " ":
                seg += 1
            prev = c

        return seg

