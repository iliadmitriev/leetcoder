#include <vector>

using std::vector;

class Solution {
public:
  bool checkXMatrix(vector<vector<int>> &grid) {
    int m = grid.size(), n = grid.back().size();

    if (m != n) {
      return false;
    }

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if ((i == j) || (m - i - 1 == j)) {
          if (grid[i][j] == 0) {
            return false;
          }
        } else {
          if (grid[i][j] != 0) {
            return false;
          }
        }
      }
    }

    return true;
  }
};