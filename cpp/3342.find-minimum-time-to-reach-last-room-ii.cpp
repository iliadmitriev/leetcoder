#include <queue>
#include <tuple>
#include <utility>
#include <vector>

using std::vector, std::pair, std::priority_queue, std::tuple;

class Solution {
public:
  int minTimeToReach(vector<vector<int>> &moveTime) {
    typedef pair<int, int> Point;
    typedef tuple<int, int, Point> State;
    const int m = moveTime.size(), n = moveTime.front().size();
    const int INF = std::numeric_limits<int>::max();
    const int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    const Point finish{m - 1, n - 1};

    vector<vector<int>> dist(m, vector<int>(n, INF));
    dist[0][0] = 0;

    priority_queue<State, vector<State>, std::greater<State>> pq;
    pq.push({0, 0, {0, 0}});

    while (pq.size()) {
      const auto [d, i, p] = pq.top();
      pq.pop();

      if (p == finish) {
        return d;
      }

      for (const auto &dir : dirs) {
        const Point np{p.first + dir[0], p.second + dir[1]};
        if (np.first < 0 || np.first >= m || np.second < 0 || np.second >= n) {
          continue;
        }

        const int nd = std::max(d, moveTime[np.first][np.second]) + 1 + i;
        if (nd < dist[np.first][np.second]) {
          dist[np.first][np.second] = nd;
          pq.push({nd, 1 - i, np});
        }
      }
    }

    return -1;
  }
};