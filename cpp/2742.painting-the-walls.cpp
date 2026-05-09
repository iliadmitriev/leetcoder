class Solution {
public:
    int paintWalls(vector<int>& cost, vector<int>& time) {
        auto n = cost.size();
        int MAX = 1e9;
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, MAX));

        // base case, left == 0 => 0
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 0;
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int left = 1; left <= n; left++) {
                dp[i][left] = min(
                    cost[i] + dp[i + 1][max(0, left - 1 - time[i])],
                    dp[i + 1][left]
                );
            }
        }

        return dp[0][n];
    }
};