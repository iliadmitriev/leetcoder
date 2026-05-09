#include <algorithm>
#include <numeric>
#include <vector>
using std::vector;

class UnionFind {
private:
  int size;
  int components;
  vector<int> rank;
  vector<int> parent;

public:
  UnionFind(int n) : size(n), components(n), rank(n), parent(n) {
    std::fill(rank.begin(), rank.end(), 1);
    std::iota(parent.begin(), parent.end(), 0);
  }

  int find(int x) {
    while (x != parent[x]) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }

    return x;
  }

  inline void dec() { components--; }

  bool join(int x, int y) {
    int parX = find(x), parY = find(y);

    if (parX == parY) {
      return false;
    }

    if (rank[parX] > rank[parY]) {
      std::swap(parX, parY);
    }

    parent[parX] = parY;
    rank[parY] += rank[parX];
    rank[parX] = 0;
    dec();
    return true;
  }

  int count() { return components; }
};

class Solution {
private:
  inline int idx(int n, int r, int c) { return n * r + c; }

  void cross(int row, int col, UnionFind *uf, const vector<vector<int>> &grid) {
    int m = grid.size(), n = grid.back().size();
    int target = m * n;

    for (int r = row - 1; r >= 0; r--) {
      if (grid[r][col]) {
        break;
      }
      uf->join(idx(n, r, col), target);
    }

    for (int r = row + 1; r < m; r++) {
      if (grid[r][col]) {
        break;
      }
      uf->join(idx(n, r, col), target);
    }

    for (int c = col - 1; c >= 0; c--) {
      if (grid[row][c]) {
        break;
      }
      uf->join(idx(n, row, c), target);
    }

    for (int c = col + 1; c < n; c++) {
      if (grid[row][c]) {
        break;
      }
      uf->join(idx(n, row, c), target);
    }
  }

public:
  int countUnguarded(int m, int n, vector<vector<int>> &guards,
                     vector<vector<int>> &walls) {
    vector<vector<int>> grid(m, vector<int>(n, 0));
    UnionFind uf = UnionFind(m * n + 1); // add 1 extra cell as "blackhole"

    for (const auto &g : guards) {
      grid[g[0]][g[1]] = 1;
      uf.dec();
    }

    for (const auto &w : walls) {
      grid[w[0]][w[1]] = 1;
      uf.dec();
    }

    for (const auto &g : guards) {
      cross(g[0], g[1], &uf, grid);
    }

    return uf.count() - 1;
  }
};