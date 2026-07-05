#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    vector<int> pathsWithMaxScore(vector<string>& board) {
        int n = board.size();
        constexpr int MOD = 1e9 + 7;
        // dp[i][j] = {max_score, count} to reach (i,j) from S
        vector<vector<pair<int, int>>> dp(n,
                                          vector<pair<int, int>>(n, {-1, 0}));
        dp[n - 1][n - 1] = {0, 1};

        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (board[i][j] == 'X' || (i == n - 1 && j == n - 1))
                    continue;

                int best = -1, ways = 0;
                // Predecessors: came from below, right, or diagonal
                for (auto [di, dj] : {pair{1, 0}, {0, 1}, {1, 1}}) {
                    int pi = i + di, pj = j + dj;
                    if (pi < n && pj < n && dp[pi][pj].first >= 0) {
                        if (dp[pi][pj].first > best) {
                            best = dp[pi][pj].first;
                            ways = dp[pi][pj].second;
                        } else if (dp[pi][pj].first == best) {
                            ways = (ways + dp[pi][pj].second) % MOD;
                        }
                    }
                }

                if (best >= 0) {
                    int val = (board[i][j] >= '1' && board[i][j] <= '9')
                                  ? board[i][j] - '0'
                                  : 0;
                    dp[i][j] = {best + val, ways};
                }
            }
        }

        return dp[0][0].first < 0
                   ? vector<int>{0, 0}
                   : vector<int>{dp[0][0].first, dp[0][0].second};
    }
};