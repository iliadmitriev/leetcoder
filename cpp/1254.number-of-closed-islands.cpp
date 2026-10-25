#include <vector>
using std::vector;

class Solution {
private:
    bool dfs_fill(vector<vector<int>>& g, int r, int c) {
        if (r < 0 || c < 0 || r >= g.size() || c >= g.front().size()) {
            return false;
        }

        if (g[r][c] == 1) {
            return true;
        }

        g[r][c] = 1;

        bool up = dfs_fill(g, r + 1, c);
        bool right = dfs_fill(g, r, c + 1);
        bool down = dfs_fill(g, r - 1, c);
        bool left = dfs_fill(g, r, c - 1);

        return up && down && left && right;
    }

public:
    int closedIsland(vector<vector<int>>& grid) {
        const int m = grid.size(), n = grid.front().size();
        int res = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) {
                    if (dfs_fill(grid, r, c)) {
                        res++;
                    }
                }
            }
        }

        return res;
    }
};
