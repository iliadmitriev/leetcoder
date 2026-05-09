#include <numeric>
#include <vector>

using std::vector;

class Solution {
private:
  bool isMagicSquare(const vector<vector<int>> &grid, int x, int y) {
    vector<int> s(10, 0);
    const int target = 15;
    int diag1 = 0, diag2 = 0;

    for (int dy = 0; dy < 3; ++dy) {
      for (int dx = 0; dx < 3; ++dx) {
        int v = grid[x + dy][y + dx];
        if (v > 9 || v < 0) {
          continue;
        }
        s[v] = 1;
      }
    }

    if (std::accumulate(s.begin(), s.end(), 0) != 9) {
      return false;
    }

    for (int d = 0; d < 3; ++d) {
      diag1 += grid[x + d][y + d];
      diag2 += grid[x + d][y + 2 - d];
    }

    if (diag1 != target || diag2 != target) {
      return false;
    }

    for (int d1 = 0; d1 < 3; ++d1) {
      int sumRow = 0, sumCol = 0;
      for (int d2 = 0; d2 < 3; ++d2) {
        sumRow += grid[x + d1][y + d2];
        sumCol += grid[x + d2][y + d1];
      }

      if (sumRow != target || sumCol != target) {
        return false;
      }
    }

    return true;
  }

public:
  int numMagicSquaresInside(vector<vector<int>> &grid) {
    int m = grid.size(), n = grid[0].size();
    int ans = 0;

    for (int i = 0; i < m - 2; ++i) {
      for (int j = 0; j < n - 2; ++j) {
        if (isMagicSquare(grid, i, j)) {
          ++ans;
        }
      }
    }

    return ans;
  }
};