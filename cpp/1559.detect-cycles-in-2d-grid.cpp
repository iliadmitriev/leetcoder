#include <numeric>
#include <vector>

using std::vector;

class UnionSet {
private:
  vector<int> par;

public:
  UnionSet(int n) : par(n) { std::iota(par.begin(), par.end(), 0); }

  /*
  find parent component for x
  */
  int find(int x) {
    while (x != par[x]) {
      par[x] = par[par[x]];
      x = par[x];
    }

    return x;
  }

  /*
  joins x and y components
  returns true if success, false if already joined
  */
  bool join(int x, int y) {
    int px = find(x), py = find(y);

    if (px == py) {
      return false;
    }

    par[px] = py;
    return true;
  }
};

class Solution {
public:
  bool containsCycle(vector<vector<char>> &grid) {
    const int m = grid.size(), n = grid.front().size();

    auto flatten = [n](int i, int j) -> int { return i * n + j; };

    UnionSet uf = UnionSet(m * n);

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        // step down i + 1
        if (i + 1 < m && grid[i][j] == grid[i + 1][j] &&
            !uf.join(flatten(i, j), flatten(i + 1, j))) {
          return true;
        }

        // stop right j + 1
        if (j + 1 < n && grid[i][j] == grid[i][j + 1] &&
            !uf.join(flatten(i, j), flatten(i, j + 1))) {
          return true;
        }
      }
    }

    return false;
  }
};