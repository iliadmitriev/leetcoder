#include <utility>
#include <vector>

using std::pair;
using std::vector;

class Solution {
public:
  Solution() {}
  int minDays(vector<vector<int>> &grid) {
    _time = 0;
    int m = grid.size(), n = grid[0].size();

    vector<vector<int>> disc(m, vector<int>(n, -1));
    vector<vector<int>> low(m, vector<int>(n, -1));
    int lands = 0, islands = 0;
    bool hasArticularPoint = false;

    for (int r = 0; r < m; ++r) {
      for (int c = 0; c < n; ++c) {
        if (grid[r][c] == 0) {
          continue;
        }

        ++lands;

        if (disc[r][c] == -1) {

          islands++;

          hasArticularPoint =
              hasArticularPointsDFS(grid, r, c, disc, low, {-1, -1}) ||
              hasArticularPoint;
        }

        // optimize
        if (islands > 1) {
          return 0;
        }
      }
    }

    if (islands != 1)
      return 0;
    else if (hasArticularPoint || lands == 1)
      return 1;
    return 2;
  }

private:
  const vector<pair<int, int>> DIRS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
  int _time;

  bool isValidLand(const vector<vector<int>> &grid, int r, int c) {
    return r >= 0 && r < grid.size() && c >= 0 && c < grid[0].size() &&
           grid[r][c] == 1;
  }

  bool hasArticularPointsDFS(const vector<vector<int>> &grid, int r, int c,
                             vector<vector<int>> &disc,
                             vector<vector<int>> &low, pair<int, int> parent) {
    disc[r][c] = low[r][c] = _time++;
    int child = 0;
    bool hasArticularPoint = false;

    for (auto [dr, dc] : DIRS) {
      int nr = r + dr, nc = c + dc;
      if (!isValidLand(grid, nr, nc))
        continue;

      if (disc[nr][nc] == -1) {
        ++child;

        hasArticularPoint =
            hasArticularPointsDFS(grid, nr, nc, disc, low, {r, c}) ||
            hasArticularPoint;

        low[r][c] = std::min(low[r][c], low[nr][nc]);

        if (parent != pair{-1, -1} && disc[r][c] <= low[nr][nc])
          hasArticularPoint = true;

      } else if (parent != pair{nr, nc}) {
        low[r][c] = std::min(low[r][c], disc[nr][nc]);
      }
    }

    if (parent == pair{-1, -1} && child > 1)
      hasArticularPoint = true;

    return hasArticularPoint;
  }
};