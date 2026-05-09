#include <queue>
#include <utility>
#include <vector>

using std::vector, std::priority_queue, std::pair;

class Solution {
public:
  int minTimeToReach(vector<vector<int>> &moveTime) {
    typedef pair<int, int> Point;
    const int m = moveTime.size(), n = moveTime[0].size();
    const int INF = std::numeric_limits<int>::max();
    const Point finish{m - 1, n - 1};
    const vector<Point> dirs{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    vector<vector<int>> dist(m, vector<int>(n, INF));
    dist[0][0] = 0;

    priority_queue<pair<int, Point>, vector<pair<int, Point>>,
                   std::greater<pair<int, Point>>>
        pq;

    pq.push({0, {0, 0}});

    while (pq.size()) {
      auto [d, p] = pq.top();
      pq.pop();

      if (p == finish) {
        return d;
      }

      for (const auto &dir : dirs) {
        const Point next{p.first + dir.first, p.second + dir.second};
        if (next.first < 0 || next.first >= m || next.second < 0 ||
            next.second >= n) {
          continue;
        }

        int nextDist = std::max(d, moveTime[next.first][next.second]) + 1;

        if (nextDist < dist[next.first][next.second]) {
          dist[next.first][next.second] = nextDist;
          pq.push({nextDist, next});
        }
      }
    }

    return -1;
  }
};