#include <vector>
using std::vector;

class Solution {
public:
  int projectionArea(vector<vector<int>> &grid) {
    int xy = 0, xz = 0, yz = 0;

    const int n = grid.size();

    for (int i = 0; i < n; ++i) {
      int x = 0, y = 0;
      for (int j = 0; j < n; ++j) {
        xy += grid[i][j] > 0 ? 1 : 0;

        x = std::max(x, grid[i][j]);
        y = std::max(y, grid[j][i]);
      }

      xz += x;
      yz += y;
    }

    return xy + xz + yz;
  }
};