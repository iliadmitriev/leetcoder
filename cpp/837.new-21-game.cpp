class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        vector<double> dp(n + maxPts, 0.0);
        for (int i = k; i <= n; i++) {
            dp[i] = 1.0;
        }

        double S = min(n - k + 1, maxPts);
        for (int i = k - 1; i >= 0; i--) {
            dp[i] = S / maxPts;
            S += dp[i] - dp[i + maxPts];
        }

        return dp[0];
    }
};