class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        lo, hi = 0, len(s)

        arr: list[int] = []
        for ch in s:
            if ch == "I":
                arr.append(lo)
                lo += 1
            else:
                arr.append(hi)
                hi -= 1

        arr.append(hi)  # or lo
        return arr

