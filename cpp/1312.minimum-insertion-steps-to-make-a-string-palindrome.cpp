class Solution {
public:
    int minInsertions(string s) {
        auto n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // slide window sizes within interval [1, n - 1]
        for (int win = 1; win < n; win++) {
            // left 
            for (int l = 0; l < n - win; l++) {
                int r = l + win;
                if (s[l] == s[r]) {
                    dp[l][r] = dp[l + 1][r - 1];
                } else {
                    dp[l][r] = 1 + min(dp[l + 1][r], dp[l][r - 1]);
                }
            }
        }

        return dp[0][n - 1];
    }
};