#include <vector>

using std::vector;

class Solution {
public:
  int surfaceArea(vector<vector<int>> &grid) {
    int area = 0;

    int m = grid.size(), n = grid.front().size();

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {

        // add 4 tiles for every 1 unit of cube column height
        // add 2 tiles for top and bottom tiles
        area += grid[i][j] * 4 + (grid[i][j] > 0) * 2;

        // discard 2 tiles for every unit of height of attachment
        // of two columns horizontally
        if (i > 0) {
          area -= std::min(grid[i][j], grid[i - 1][j]) * 2;
        }

        // discard 2 tiles for 1 unit of height of attachment vertically
        if (j > 0) {
          area -= std::min(grid[i][j], grid[i][j - 1]) * 2;
        }
      }
    }

    return area;
  }
};