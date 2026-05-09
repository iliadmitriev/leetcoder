class Solution {
private:
  vector<pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

  int dfs(const vector<vector<int>> &grid, int r, int c, int maxGold,
          vector<vector<bool>> &visited) {
    if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() ||
        visited[r][c] || grid[r][c] == 0) {
      return 0;
    }

    int res = 0;
    visited[r][c] = true;

    for (auto [nr, nc] : dirs) {
      res = max(res, dfs(grid, nr + r, nc + c, maxGold, visited));
    }
    visited[r][c] = false;

    res += grid[r][c];
    return res;
  }

public:
  int getMaximumGold(vector<vector<int>> &grid) {

    int ROWS = grid.size(), COLS = grid[0].size();
    vector<vector<bool>> visited(ROWS, vector<bool>(COLS, false));
    int maxGold = 0;

    for (int r = 0; r < ROWS; r++) {
      for (int c = 0; c < COLS; c++) {
        if (visited[r][c] || grid[r][c] == 0) {
          continue;
        }

        maxGold = max(maxGold, dfs(grid, r, c, maxGold, visited));
      }
    }

    return maxGold;
  }
};