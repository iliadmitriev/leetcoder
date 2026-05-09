#include <algorithm>
#include <vector>

using std::max;
using std::sort;
using std::vector;

class Solution {
public:
  int deleteGreatestValue(vector<vector<int>> &grid) {
    for (auto &row : grid) {
      sort(row.rbegin(), row.rend());
    }

    int ans = 0;

    int m = grid.size(), n = grid[0].size();

    for (int j = 0; j < n; j++) {
      int maxRow = grid[0][j];
      for (int i = 1; i < m; i++) {
        maxRow = max(maxRow, grid[i][j]);
      }

      ans += maxRow;
    }

    return ans;
  }
};