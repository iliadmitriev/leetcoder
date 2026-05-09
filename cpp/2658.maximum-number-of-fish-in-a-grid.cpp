#include <vector>

using std::vector;
class Solution {
public:
  int findMaxFish(vector<vector<int>> &grid) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<bool>> vis(m, vector<bool>(n, false));
    int maxComponentWeight = 0;

    for (int r = 0; r < m; r++) {
      for (int c = 0; c < n; c++) {
        if (grid[r][c] == 0 || vis[r][c]) {
          continue;
        }

        maxComponentWeight = std::max(maxComponentWeight, dfs(r, c, vis, grid));
      }
    }

    return maxComponentWeight;
  }

private:
  int dfs(int r, int c, vector<vector<bool>> &vis,
          const vector<vector<int>> &grid) {
    int m = grid.size(), n = grid[0].size();
    if (r < 0 || r >= m || c < 0 || c >= n || vis[r][c] || grid[r][c] == 0) {
      return 0;
    }

    vis[r][c] = true;

    return grid[r][c] + dfs(r - 1, c, vis, grid) + dfs(r + 1, c, vis, grid) +
           dfs(r, c - 1, vis, grid) + dfs(r, c + 1, vis, grid);
  }
};