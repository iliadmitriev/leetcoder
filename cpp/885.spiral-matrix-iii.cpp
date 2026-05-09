#include <utility>
#include <vector>

using std::pair;
using std::vector;

class Solution {
private:
  inline bool fit(int y, int x, int rows, int cols) {
    return 0 <= y && y < rows && 0 <= x && x < cols;
  }

public:
  vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart,
                                      int cStart) {
    vector<vector<int>> coords;
    coords.reserve(rows * cols);

    int r = rStart, c = cStart;
    int cycle = 1; // changes every 2 loops
    int dir = 0;   // 0: right, 1: down, 2: left, 3: up; changes every 1 loops
    vector<pair<int, int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    for (int i = 0; coords.size() < rows * cols; i++) {
      for (int j = 0; j < cycle; j++) {
        if (fit(r, c, rows, cols)) {
          coords.push_back({r, c});
        }
        r += dirs[dir].first;
        c += dirs[dir].second;
      }

      cycle += i % 2;
      dir = (dir + 1) % 4;
    }

    return coords;
  }
};