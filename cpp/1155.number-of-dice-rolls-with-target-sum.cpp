const int MOD = int(1e9) + 7;

class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        if (target < n || target > n * k) {
            return 0;
        }

        vector<vector<int>> dp(target + 1, vector<int>(n + 1, 0));
        dp[0][0] = 1;

        for (int x = 1; x <= n; x++) {
            for (int t = target; t >=0; t--) {
                for (int i = 1; i <= k; i++) {
                    if (t >= i) {
                        dp[t][x] += dp[t - i][x - 1];
                        dp[t][x] %= MOD;
                    }
                }
            }
        }

        return dp[target][n];
    }
};