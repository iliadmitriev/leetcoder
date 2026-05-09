#include <vector>

using std::vector;

class Solution {
private:
    inline int cost(int val) { return val == 0 ? 0 : 1; }

public:
    int maxPathScore(vector<vector<int>>& grid, int k) {
        const int m = grid.size(), n = grid.front().size();
        const int negInf = std::numeric_limits<int>::min();

        // dp[row][col][cost] = score
        vector<vector<vector<int>>> dp(
            m, vector<vector<int>>(n, vector<int>(k + 1, negInf)));
        // if score == negInf, reached limit of k cost
        dp[0][0][0] = 0; // start at 0,0 with 0 score and 0 cost

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int c = 0; c <= k; c++) {
                    if (dp[i][j][c] == negInf) {
                        continue;
                    }

                    // go down if possible
                    if (i + 1 < m) {
                        int val = grid[i + 1][j]; // extra score
                        int valCost = cost(val);  // extra cost

                        // if total cost is not exceeded
                        if (c + valCost <= k) {
                            dp[i + 1][j][c + valCost] = std::max(
                                dp[i + 1][j][c + valCost], dp[i][j][c] + val);
                        }
                    }

                    // go right if possible
                    if (j + 1 < n) {
                        int val = grid[i][j + 1]; // possible extra score
                        int valCost = cost(val);  // possible cost

                        // if total cost is not exceeded
                        if (c + valCost <= k) {
                            dp[i][j + 1][c + valCost] = std::max(
                                dp[i][j + 1][c + valCost], dp[i][j][c] + val);
                        }
                    }
                }
            }
        }

        int res = ranges::max(dp[m - 1][n - 1]);

        return res < 0 ? -1 : res;
    }
};