class Solution {
private:
  int max2d(const vector<vector<int>> &grid, int r, int c, int kernel) {
    int res = grid[r][c];
    for (int i = r; i < r + kernel; ++i) {
      for (int j = c; j < c + kernel; ++j) {
        res = max(res, grid[i][j]);
      }
    }
    return res;
  }

public:
  vector<vector<int>> largestLocal(vector<vector<int>> &grid) {
    int n = grid.size() - 2;
    vector<vector<int>> res(n, vector<int>(n));

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        res[i][j] = max2d(grid, i, j, 3);
      }
    }

    return res;
  }
};