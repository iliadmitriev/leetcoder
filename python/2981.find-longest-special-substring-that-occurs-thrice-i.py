from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        def check(s: str, targetLen: int) -> bool:
            count = defaultdict(int)

            for i in range(len(s) - targetLen + 1):
                key = "".join(set(s[i: i + targetLen]))

                if len(key) > 1:
                    continue

                count[key] += 1
                if count[key] == 3:
                    return True

            return False

        lo, hi = 0, len(s)
        while lo < hi:
            mid = (lo + hi) // 2

            if check(s, mid):
                lo = mid + 1
            else:
                hi = mid

        lo -= 1
        if lo == 0:
            return -1

        return lo

