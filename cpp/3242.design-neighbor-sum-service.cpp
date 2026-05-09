#include <unordered_map>
#include <utility>
#include <vector>

using std::pair;
using std::unordered_map;
using std::vector;

class neighborSum {
private:
  int M, N;
  vector<vector<int>> _grid;
  unordered_map<int, pair<int, int>> data;

  int nodeIter(pair<int, int> start, vector<pair<int, int>> nodes) {
    auto [y, x] = start;
    int res = 0;
    for (auto [dy, dx] : nodes) {
      int ny = y + dy;
      int nx = x + dx;
      if (0 <= ny && ny < M && 0 <= nx && nx < N) {
        res += _grid[ny][nx];
      }
    }
    return res;
  }

public:
  neighborSum(vector<vector<int>> &grid)
      : _grid(grid), M(grid.size()), N(grid[0].size()) {
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        data[grid[i][j]] = {i, j};
      }
    }
  }

  int adjacentSum(int value) {
    if (!data.count(value)) {
      return 0;
    }

    return nodeIter(data[value], {{-1, 0}, {0, 1}, {1, 0}, {0, -1}});
  }

  int diagonalSum(int value) {
    if (!data.count(value)) {
      return 0;
    }

    return nodeIter(data[value], {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}});
  }
};

/**
 * Your neighborSum object will be instantiated and called as such:
 * neighborSum* obj = new neighborSum(grid);
 * int param_1 = obj->adjacentSum(value);
 * int param_2 = obj->diagonalSum(value);
 */