#include <limits>
#include <queue>
#include <vector>

using std::vector, std::priority_queue, std::pair, std::greater;

class Solution {
public:
  int countPaths(int n, vector<vector<int>> &roads) {
    const long INF = std::numeric_limits<long>::max();
    const int MOD = int(1e9) + 7;

    vector<vector<pair<int, int>>> adj(n);
    priority_queue<pair<long, int>, vector<pair<long, int>>,
                   greater<pair<long, int>>>
        pq;
    vector<long> count(n, 0);
    vector<long> dist(n, INF);

    for (const auto &r : roads) {
      adj[r[0]].push_back({r[1], r[2]});
      adj[r[1]].push_back({r[0], r[2]});
    }

    pq.push({0, 0});
    count[0] = 1;
    dist[0] = 0;

    while (pq.size()) {
      auto [nodeDist, node] = pq.top();
      pq.pop();

      for (auto [next, w] : adj[node]) {
        if (nodeDist + w < dist[next]) {
          count[next] = count[node];
          dist[next] = nodeDist + w;
          pq.push({dist[next], next});

        } else if (nodeDist + w == dist[next]) {
          count[next] += count[node];
          count[next] %= MOD;
        }
      }
    }

    return count[n - 1];
  }
};