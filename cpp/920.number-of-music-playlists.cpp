class Solution {
public:
    int numMusicPlaylists(int n, int goal, int k) {
        long dp[goal + 1][n + 1];
        memset(dp, 0, sizeof(dp));
        long mod = 1e9 + 7;
        dp[0][0] = 1;

        for (int i = 1; i <= goal; i++)
            for (int j = 1; j <= min(i, n); j++)
                dp[i][j] = (
                    dp[i - 1][j - 1] * (n - (j - 1))
                    + (j > k ? dp[i - 1][j] * (j - k) : 0)
                ) % mod;
        return dp[goal][n];
    }
};