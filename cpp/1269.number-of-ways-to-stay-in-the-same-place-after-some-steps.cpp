class Solution {
public:
    int numWays(int steps, int arrLen) {
        int MOD = 1e9 + 7;
        arrLen = min(steps / 2 + 1, arrLen);
        vector<vector<int> > dp(steps + 1, vector<int>(arrLen, 0));

        // base case
        dp[0][0] = 1;

        for (int step = 1; step <= steps; step++) {
            for (int pos = arrLen - 1; pos >= 0; pos--) {
                long res = dp[step - 1][pos];
                if (pos > 0) {
                    res += dp[step - 1][pos - 1];
                }
                if (pos < arrLen - 1) {
                    res += dp[step - 1][pos + 1];
                }
                dp[step][pos] = res % MOD;
            }
        }
        return dp[steps][0];
    }
};