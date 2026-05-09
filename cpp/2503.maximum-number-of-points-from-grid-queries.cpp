#include <functional>
#include <numeric>
#include <queue>
#include <vector>

using std::vector, std::pair, std::priority_queue, std::greater;

class Solution {
public:
  vector<int> maxPoints(vector<vector<int>> &grid, vector<int> &queries) {
    typedef pair<int, int> P;
    typedef pair<int, P> Q;

    const vector<P> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    const int m = grid.size(), n = grid[0].size();
    const int k = queries.size();
    int count = 0;
    vector<int> res(k, 0);
    vector<int> idxs(k);
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    priority_queue<Q, vector<Q>, greater<>> q;

    visited[0][0] = true;
    q.push(Q(grid[0][0], P(0, 0)));

    std::iota(idxs.begin(), idxs.end(), 0);
    std::sort(idxs.begin(), idxs.end(), [&queries](int i, int j) -> bool {
      return queries[i] < queries[j];
    });

    for (int i : idxs) {

      while (q.size() && q.top().first < queries[i]) {
        auto [r, c] = q.top().second;
        q.pop();
        count++;

        for (auto [dr, dc] : dirs) {
          int nr = r + dr, nc = c + dc;
          if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]) {
            continue;
          }

          visited[nr][nc] = true;
          q.push(Q(grid[nr][nc], P(nr, nc)));
        }
      }

      res[i] = count;
    }

    return res;
  }
};