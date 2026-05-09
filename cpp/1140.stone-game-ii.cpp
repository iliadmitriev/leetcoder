class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        int INF = std::numeric_limits<int>::min() >> 1;

        // prefix sum of piles, starting from 0
        vector<int> s(n + 1, 0);
        partial_sum(piles.begin(), piles.end(), s.begin() + 1);
        
        // dp memo table (initialized with -infinity)
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, INF));

        for (int pos = n; pos >= 0; pos--) {
            for (int m = n; m >= 1; m--) {
                if (pos + m + m >= n) {
                    // player can take the rest of piles
                    dp[pos][m] = s[n] - s[pos];
                } else {
                    for (int step = 1; step <= m + m; step++) {
                        dp[pos][m] = max(
                            dp[pos][m],
                            s[pos + step] - s[pos] - dp[pos + step][max(m, step)]
                        );
                    }
                }
            }
        }

        return (s[n] + dp[0][1]) / 2;
    }
};