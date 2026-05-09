#include <vector>
using std::vector;

class Solution {
public:
    long long maximumScore(vector<vector<int>>& grid) {
        const int n = grid.size();

        if (n == 1) {
            return 0;
        }

        // columnar prefix[row, col agg]
        vector<vector<long long>> col(n, vector<long long>(n + 1, 0));
        // dp table []
        vector<vector<vector<long long>>> dp(
            n, vector<vector<long long>>(n + 1, vector<long long>(2, 0)));

        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) {
                col[i][j + 1] = col[i][j] + grid[j][i];
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j0 = 0; j0 <= n; j0++) {
                long long p0 = dp[i - 1][j0][0];
                long long p1 = dp[i - 1][j0][1];

                for (int j1 = 0; j1 <= n; j1++) {
                    bool isGreater = j1 > j0;

                    long long prevX =
                        isGreater ? (col[i - 1][j1] - col[i - 1][j0]) : 0;
                    long long currX =
                        !isGreater ? (col[i][j0] - col[i][j1]) : 0;

                    // state 0: score in cur col exclusive
                    dp[i][j1][0] =
                        std::max(dp[i][j1][0], std::max(prevX + p0, p1));

                    // state 1: score in cur col inclusive
                    dp[i][j1][1] = std::max(dp[i][j1][1],
                                            currX + std::max(p1, prevX + p0));
                }
            }
        }

        long long res = 0;
        for (int j = 0; j <= n; j++) {
            res = std::max(res, dp[n - 1][j][1]);
        }

        return res;
    }
};