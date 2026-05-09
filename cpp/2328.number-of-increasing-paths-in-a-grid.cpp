class Solution {
public:
    int countPaths(vector<vector<int>>& grid) {
        int mod = 1e9 + 7;
        int m = grid.size(); int n = grid[0].size();

        vector<pair<int, int>> cells;
        cells.reserve(m * n);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cells.push_back({i, j});
            }
        }

        std::sort(cells.begin(), cells.end(), [&grid](auto& p1, auto& p2) {
            return grid[p1.first][p1.second] < grid[p2.first][p2.second];
        });
        
        vector<pair<int, int>> steps = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        vector<vector<int>> dp(m, vector<int>(n, 1));

        for (auto [i, j] : cells) {
            for (auto [di, dj] : steps) {
                int y = i + di; int x = j + dj;
                if (0 <= y && y < m && 0 <= x && x < n && grid[i][j] < grid[y][x]) {
                    dp[y][x] += dp[i][j];
                    dp[y][x] %= mod;
                }
            }
        }

        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res += dp[i][j];
                res %= mod;
            }
        }

        return res;
    }
};