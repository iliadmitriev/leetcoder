#include <string>
#include <vector>

using std::vector;

class Solution {
private:
  int inline digitLen(int x) { return std::to_string(x).length(); }

public:
  vector<int> findColumnWidth(vector<vector<int>> &grid) {
    int m = grid.size(), n = grid.front().size();

    vector<int> res(n);

    for (int j = 0; j < n; ++j) {
      int maxLen = 0;

      for (int i = 0; i < m; ++i) {
        maxLen = std::max(maxLen, digitLen(grid[i][j]));
      }

      res[j] = maxLen;
    }

    return res;
  }
};