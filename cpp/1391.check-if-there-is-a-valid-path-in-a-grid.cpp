#include <numeric>
#include <vector>

using std::vector;

class Solution {
public:
    inline int flatten(int r, int c, int n) { return r * n + c; }
    inline bool toLeft(int v) { return v == 1 || v == 3 || v == 5; }
    inline bool toRight(int v) { return v == 1 || v == 4 || v == 6; }
    inline bool toTop(int v) { return v == 2 || v == 5 || v == 6; }
    inline bool toBottom(int v) { return v == 2 || v == 3 || v == 4; }

    // 0 - bottom, 1 - left, 2 - top, 3 - right
    static constexpr int dirs[] = {1, 0, -1, 0, 1};

    inline bool connected(int i, int j, int dir, vector<vector<int>>& grid) {
        switch (dir) {
        case 0: // bottom
            return toBottom(grid[i][j]) && toTop(grid[i + 1][j]);
        case 1: // left
            return toLeft(grid[i][j]) && toRight(grid[i][j - 1]);
        case 2: // top
            return toTop(grid[i][j]) && toBottom(grid[i - 1][j]);
        case 3: // right
            return toRight(grid[i][j]) && toLeft(grid[i][j + 1]);
        }
        return false;
    }

    inline bool fit(int i, int j, int m, int n) {
        return i >= 0 && i < m && j >= 0 && j < n;
    }

    // i,j - current cell; pi,pj - previous cell
    bool dfs(int i, int j, int pi, int pj, vector<vector<int>>& grid) {
        const int m = grid.size(), n = grid.front().size();

        // if came back to an origin (started in a loop)
        if (i == 0 && j == 0 && !(pi == -1 && pj == -1)) {
            return false;
        }

        if (i == m - 1 && j == n - 1) {
            return true;
        }

        for (int dir = 0; dir < 4; dir++) {
            int ni = i + dirs[dir], nj = j + dirs[dir + 1]; // next cell

            if (!fit(ni, nj, m, n)) { // it should be in the bounds
                continue;
            }

            if (pi == ni && pj == nj) { // do not step to previous cell
                continue;
            }

            // if current cell is connected to a cell in direction
            // and this connection leads to success, then return true
            if (connected(i, j, dir, grid) && dfs(ni, nj, i, j, grid)) {
                return true;
            }
        }

        return false;
    }

    bool hasValidPath(vector<vector<int>>& grid) {
        return dfs(0, 0, -1, -1, grid);
    }
};