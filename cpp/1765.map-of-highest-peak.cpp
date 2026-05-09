#include <queue>
#include <utility>
#include <vector>

using std::vector, std::queue, std::pair;

class Solution {
public:
  vector<vector<int>> highestPeak(vector<vector<int>> &isWater) {
    const int m = isWater.size(), n = isWater.back().size();
    const vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    vector<vector<int>> res(m, vector<int>(n, -1));

    queue<pair<int, int>> q;
    for (int r = 0; r < m; ++r) {
      for (int c = 0; c < n; ++c) {
        if (isWater[r][c] == 0) {
          continue;
        }

        q.push({r, c});
        res[r][c] = 0;
      }
    }

    while (!q.empty()) {
      auto [r, c] = q.front();
      q.pop();

      for (auto [dr, dc] : dirs) {
        int nr = r + dr, nc = c + dc;

        if (nr < 0 || nr >= m || nc < 0 || nc >= n || res[nr][nc] != -1) {
          continue;
        }

        res[nr][nc] = res[r][c] + 1;
        q.push({nr, nc});
      }
    }

    return res;
  }
};