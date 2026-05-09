#include <vector>
using std::vector;

class Solution {
private:
  // count minimal square size in matrix statring from top left (r1, c1)
  // and ending at bottom left (r2, c2)
  int countMinSquare(const vector<vector<int>> &grid, int r1, int c1, int r2,
                     int c2) {
    int left = c2, right = c1, top = r2,
        bottom = r1; // init worst as worst case

    for (int i = r1; i < r2; i++) {
      for (int j = c1; j < c2; j++) {
        if (grid[i][j] == 1) {
          left = std::min(left, j);
          right = std::max(right, j);
          top = std::min(top, i);
          bottom = std::max(bottom, i);
        }
      }
    }

    int height = bottom - top + 1, width = right - left + 1;

    if (height > 0 && width > 0) {
      return height * width;
    }

    return 0;
  }

public:
  /*
   * Time: O(m^3 * n^3)
   * Space: O(1)
   */
  int minimumSum(vector<vector<int>> &grid) {
    const int m = grid.size(), n = grid.front().size();
    int total = m * n;

    // try all horizontal splits in 3 non empty parts
    for (int r1 = 1; r1 < m - 1; r1++) {
      for (int r2 = r1 + 1; r2 < m; r2++) {
        total = std::min(total, countMinSquare(grid, 0, 0, r1, n) +
                                    countMinSquare(grid, r1, 0, r2, n) +
                                    countMinSquare(grid, r2, 0, m, n));
      }
    }

    // try all vertical possible non-empty splits in 3 parts
    for (int c1 = 1; c1 < n - 1; c1++) {
      for (int c2 = c1 + 1; c2 < n; c2++) {
        total = std::min(total, countMinSquare(grid, 0, 0, m, c1) +
                                    countMinSquare(grid, 0, c1, m, c2) +
                                    countMinSquare(grid, 0, c2, m, n));
      }
    }

    // try all possible vertical and then horisontal split
    // also all possible horizontal and then veritcal
    // in 3 non-empty parts
    for (int r = 1; r < m; r++) {
      for (int c = 1; c < n; c++) {
        // horizontal and then vertical (top, bottom left and bottom right
        // parts)
        total = std::min(total, countMinSquare(grid, 0, 0, r, n) +
                                    countMinSquare(grid, r, 0, m, c) +
                                    countMinSquare(grid, r, c, m, n));
        // horizontal and then vertical (bottom, top left, top right)
        total = std::min(total, countMinSquare(grid, r, 0, m, n) +
                                    countMinSquare(grid, 0, 0, r, c) +
                                    countMinSquare(grid, 0, c, r, n));
        // vertical and then horizontal (left, top right, bottom right)
        total = std::min(total, countMinSquare(grid, 0, 0, m, c) +
                                    countMinSquare(grid, 0, c, r, n) +
                                    countMinSquare(grid, r, c, m, n));
        // vertical and then horizontal (right, top left, top right)
        total = std::min(total, countMinSquare(grid, 0, c, m, n) +
                                    countMinSquare(grid, 0, 0, r, c) +
                                    countMinSquare(grid, r, 0, m, c));
      }
    }

    return total;
  }
};