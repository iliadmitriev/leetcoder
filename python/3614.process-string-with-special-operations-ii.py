class Solution:
    def processStr(self, s: str, k: int) -> str:
        size = 0

        for ch in s:
            if ch == "*":  # remove char
                size = max(0, size - 1)
            elif ch == "#":  # double
                size *= 2
            elif ch == "%":  # reverse
                pass  # lenght doesn't change
            else:  # symbol
                size += 1  # +1

        if k >= size:
            return "."

        for ch in reversed(s):
            if ch == "*":  # invert remove char (add)
                size += 1
            elif ch == "#":  # invert duplication (cut in half)
                half = size // 2

                if k >= half:  # only affects indexation if k is in 2nd half
                    k -= half  # shift index

                size = half
            elif ch == "%":  # invert revesing
                k = size - 1 - k  # reverse indexation
            else:  # symbol adding
                if k == size - 1:
                    return ch  # if it's k-th then return

                size -= 1  # else remove

        return "."
