#include <queue>
#include <utility>
#include <vector>

using std::vector, std::priority_queue, std::pair;
class Solution {
public:
  int minimumTime(vector<vector<int>> &grid) {
    if (grid[0][1] > 1 && grid[1][0] > 1) {
      return -1;
    }

    const int INF = int(1e9);
    const int m = grid.size(), n = grid[0].size();
    const pair<int, int> dirs[] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    const pair<int, int> goal = {m - 1, n - 1};

    vector<vector<int>> timer(m, vector<int>(n, INF));
    timer[0][0] = 0;

    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>,
                   std::greater<>>
        q;
    q.push({0, {0, 0}});

    while (q.size()) {
      auto [time, node] = q.top();
      q.pop();

      if (node == goal) {
        return time;
      }

      auto [y, x] = node;

      for (auto [dy, dx] : dirs) {
        int ny = y + dy, nx = x + dx;

        if (ny < 0 || nx < 0 || ny >= m || nx >= n) {
          continue;
        }

        int nextTime;
        if (time >= grid[ny][nx]) {
          nextTime = time + 1;
        } else {
          nextTime = grid[ny][nx] + (grid[ny][nx] - time - 1) % 2;
        }

        if (nextTime < timer[ny][nx]) {
          timer[ny][nx] = nextTime;
          q.push({nextTime, {ny, nx}});
        }
      }
    }

    return -1;
  }
};