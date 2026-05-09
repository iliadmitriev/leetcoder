

class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        """
        [1, 2,  4, 5, 0]
        [3, 7, 11, 9, 5]
        """

        N = len(stations)
        diff = [0] * (N + 1)
        for i in range(N):
            left = max(0, i - r)
            right = min(N, i + r + 1)
            diff[left] += stations[i]
            diff[right] -= stations[i]

        def can_achieve(x: int) -> bool:
            cur_p = 0
            cur_k = k
            cur_diff = diff.copy()

            for i in range(N):
                cur_p += cur_diff[i]

                if cur_p < x:
                    add = x - cur_p
                    if add > cur_k:
                        return False
                    cur_k -= add
                    cur_p += add
                    right = min(N, i + 2 * r + 1)
                    cur_diff[right] -= add

            return True

        lo, hi = min(stations), sum(stations) + k + 1
        res = lo

        while lo < hi:
            mid = (lo + hi) // 2

            if can_achieve(mid):
                lo = mid + 1
                res = mid
            else:
                hi = mid

        return res

