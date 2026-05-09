from itertools import accumulate


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        s = list(accumulate(piles, initial=0))
        n = len(piles)

        game = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n, -1, -1):
            for m in range(n, -1, -1):
                if i + 2 * m > n:
                    # be greedy if player can take the rest of the pile
                    game[i][m] = s[n] - s[i]
                else:
                    game[i][m] = max(
                        (
                            # max number of stones minus
                            # other player's number of stones
                            # (maximizing negative value
                            # is minimizing positive value)
                            s[j + i] - s[i] - game[i + j][max(j, m)]
                            for j in range(1, 2 * m + 1)
                        ),
                        default=0,
                    )

        return (s[n] + game[0][1]) // 2

