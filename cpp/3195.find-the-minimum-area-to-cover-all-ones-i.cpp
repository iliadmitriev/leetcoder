#include <vector>
using std::vector;

class Solution {
public:
  int minimumArea(vector<vector<int>> &grid) {
    const int m = grid.size(), n = grid.front().size();
    int left = n, right = -1, top = m, bottom = -1;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          left = std::min(left, j);
          right = std::max(right, j);
          top = std::min(top, i);
          bottom = std::max(bottom, i);
        }
      }
    }

    return (right - left + 1) * (bottom - top + 1);
  }
};