#include <deque>
#include <iostream>
#include <utility>
#include <vector>

using std::vector, std::deque, std::pair;

const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  int minimumObstacles(vector<vector<int>> &grid) {
    const int INF = int(1e9);
    const int m = grid.size(), n = grid[0].size();
    const pair<int, int> finish = {m - 1, n - 1};
    const pair<int, int> dirs[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    vector<vector<int>> dist(m, vector<int>(n, INF));
    dist[0][0] = 0;

    deque<pair<int, int>> pq;
    pq.push_back({0, 0});

    while (pq.size()) {
      auto node = pq.front();
      auto [y, x] = node;
      pq.pop_front();

      if (node == finish) {
        return dist[y][x];
      }

      for (auto [dx, dy] : dirs) {
        auto child = pair{y + dy, x + dx};
        auto [ny, nx] = child;

        if (ny < 0 || ny >= m || nx < 0 || nx >= n) {
          continue;
        }

        if (dist[ny][nx] <= dist[y][x] + grid[ny][nx]) {
          continue;
        }

        dist[ny][nx] = dist[y][x] + grid[ny][nx];
        if (grid[ny][nx] == 0) {
          pq.push_front(child);
        } else {
          pq.push_back(child);
        }
      }
    }

    return (m - 1) + (n - 1);
  }
};