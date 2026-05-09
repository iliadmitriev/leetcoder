class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int m = grid.size(); int n = grid[0].size();
        vector<vector<vector<int>>> dp(2, vector<vector<int>>(n, vector<int>(n, 0)));
        vector<pair<int, int>> dirs({{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 0}, {0, 1}, {1, -1}, {1, 0}, {1, 1}});

        for (int r = m - 1; r >= 0; r--) {
            for (int c1 = 0; c1 < n - 1; c1++) {
                for (int c2 = c1 + 1; c2 < n; c2++) {
                    int res = 0;
                    for (auto [d1, d2]: dirs) {
                        if ((c1 + d1 < 0) || (c2 + d2 >= n)) {
                            continue;
                        }

                        res = max(res, dp[(r + 1) % 2][c1 + d1][c2 + d2]);
                    }
                    dp[r % 2][c1][c2] = res + grid[r][c1] + grid[r][c2];
                }
            }
        }

        
        return dp[0][0][n - 1];
    }
};