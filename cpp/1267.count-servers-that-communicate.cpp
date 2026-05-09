#include <vector>

using std::vector;

class Solution {
public:
  int countServers(vector<vector<int>> &grid) {
    const int NROWS = grid.size(), NCOLS = grid.back().size();
    int count = 0;
    vector<int> adjRow(NROWS), adjCol(NCOLS);

    for (int r = 0; r < NROWS; r++) {
      for (int c = 0; c < NCOLS; c++) {
        if (grid[r][c] == 1) {
          adjRow[r]++;
          adjCol[c]++;
        }
      }
    }

    for (int r = 0; r < NROWS; r++) {
      for (int c = 0; c < NCOLS; c++) {
        if (grid[r][c] == 1 && (adjRow[r] > 1 || adjCol[c] > 1)) {
          count++;
        }
      }
    }
    return count;
  }
};