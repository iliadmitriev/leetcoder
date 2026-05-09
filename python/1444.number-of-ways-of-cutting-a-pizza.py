class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # m - rows count, n - cols count
        m, n = len(pizza), len(pizza[0])

        # init dp[k][rows+1][cols+1] with zero fill
        # where k - remaining cuts left
        # rows - number of rows m + 1
        # cols - number of columns n + 1
        dp = [[[0] * n for _ in range(m)] for _ in range(k)]

        # build accumulative 2D matrix for apples
        # for fast calculating (O(1)) of apple count in rectangle region
        # init dp base case
        # if there is an apples in rectangle [0, 0] - [row - 1, col - 1]
        # then it's a single way of cutting pizza with 0 cuts
        apples = [[0] * (n + 1) for _ in range(m + 1)]
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                apples[row][col] = int(pizza[row][col] == 'A') + apples[row + 1][col] + apples[row][col + 1] - apples[row + 1][col + 1]
                dp[0][row][col] = int(apples[row][col] > 0)
                
        mod = 1000000007
        for remain in range(1, k):
            for row in range(m):
                for col in range(n):
                    # next remaining cuts is calcualted by
                    # considering all possible horizontal cuts and
                    # considering all possible vertical cuts
                    dp[remain][row][col] =  sum([
                        sum(
                            dp[remain - 1][next_row][col]
                            for next_row in range(row + 1, m)
                            if apples[row][col] - apples[next_row][col] > 0
                        ),
                        sum(
                            dp[remain - 1][row][next_col]
                            for next_col in range(col + 1, n)
                            if apples[row][col] - apples[row][next_col] > 0
                        )
                    ]) % mod
        return dp[k - 1][0][0]