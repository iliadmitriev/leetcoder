import bisect


class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        n = len(events)
        events.sort()

        # cache: list[list[int | None]] = [[None] * (k + 1) for _ in range(n)]
        #
        # def dp(i: int, j: int) -> int:
        #     """
        #     i: index of event
        #     j: number of events that can be attended
        #     """
        #     if i == n or j == 0:
        #         return 0
        #
        #     res = cache[i][j]
        #     if res is not None:
        #         return res
        #
        #     # take
        #     next_i = bisect.bisect_right(
        #         events, events[i][1], lo=i, hi=n, key=lambda x: x[0]
        #     )
        #     take = events[i][2] + dp(next_i, j - 1)
        #
        #     # or leave
        #     leave = dp(i + 1, j)
        #
        #     res = max(take, leave)
        #     cache[i][j] = res
        #     return res

        dp: list[list[int]] = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            next_i = bisect.bisect_right(events, events[i][1], key=lambda x: x[0])

            for j in range(1, k + 1):
                dp[i][j] = max(
                    events[i][2] + dp[next_i][j - 1],  # take
                    dp[i + 1][j],  # leave
                )

        return dp[0][k]

