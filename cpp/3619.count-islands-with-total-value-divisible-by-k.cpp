class Solution {
public:
    int countIslands(vector<vector<int>>& grid, int k) {
        const int m = grid.size(), n = grid.front().size();
        int count = 0;

        auto dfs = [&grid, &m, &n](this auto const& self, int r, int c) -> long {
            long res = grid[r][c];
            grid[r][c] = 0;

            if (r + 1 < m && grid[r + 1][c] != 0) {
                res += self(r + 1, c);
            }

            if (r - 1 >= 0 && grid[r - 1][c] != 0) {
                res += self(r - 1, c);
            }

            if (c + 1 < n && grid[r][c + 1] != 0) {
                res += self(r, c + 1);
            }

            if (c - 1 >= 0 && grid[r][c - 1] != 0) {
                res += self(r, c - 1);
            }

            return res;
        };

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) {
                    continue;
                }

                if (dfs(r, c) % k == 0) {
                    count++;
                }
            }
        }

        return count;
    }
};