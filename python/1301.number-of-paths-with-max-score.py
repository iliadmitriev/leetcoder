class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7

        # dp[i][j] = (max_score, count)
        dp = [[(-1, 0)] * n for _ in range(n)]
        dp[n - 1][n - 1] = (0, 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "X" or (i == n - 1 and j == n - 1):
                    continue

                best, ways = -1, 0

                for di, dj in ((1, 0), (0, 1), (1, 1)):
                    pi, pj = i + di, j + dj

                    if pi < n and pj < n and dp[pi][pj][0] != -1:
                        score, count = dp[pi][pj]

                        if score > best:
                            best, ways = score, count
                        elif score == best:
                            ways = (ways + count) % MOD

                if best != -1:
                    val = int(board[i][j]) if "1" <= board[i][j] <= "9" else 0
                    dp[i][j] = (best + val, ways)

        if dp[0][0][0] == -1:
            return [0, 0]

        return list(dp[0][0])
