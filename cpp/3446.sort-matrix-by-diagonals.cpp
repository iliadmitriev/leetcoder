#include <vector>
using std::vector;

class Solution {
private:
  void sorter(vector<vector<int>> &grid, vector<int> &buf, int r, int c,
              bool rev) {
    if (r >= grid.size() || c >= grid.size()) {
      if (rev) {
        std::sort(buf.begin(), buf.end(), std::greater<int>());
      } else {
        std::sort(buf.begin(), buf.end());
      }
      return;
    }

    buf.push_back(grid[r][c]);
    sorter(grid, buf, r + 1, c + 1, rev);
    grid[r][c] = buf.back();
    buf.pop_back();
  }

public:
  vector<vector<int>> sortMatrix(vector<vector<int>> &grid) {
    const int n = grid.size();
    vector<int> buf;

    for (int i = 0; i < n; i++) {
      sorter(grid, buf, i, 0, true);
    }

    for (int j = 1; j < n; j++) {
      sorter(grid, buf, 0, j, false);
    }

    return grid;
  }
};