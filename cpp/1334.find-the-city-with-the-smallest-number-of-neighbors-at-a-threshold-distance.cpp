#include <queue>
#include <utility>
#include <vector>

using std::pair;
using std::priority_queue;
using std::vector;

class Solution {
private:
  int dijkstra(int src, int thresh, int n,
               const vector<vector<pair<int, int>>> &adj) {
    const int INF = 1e9;
    vector<int> dist(n, INF);
    dist[src] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>,
                   std::greater<pair<int, int>>>
        pq;

    pq.push({0, src});

    while (pq.size()) {
      auto [d, u] = pq.top();
      pq.pop();

      if (d > thresh)
        continue;

      for (auto [v, w] : adj[u]) {
        if (d + w >= dist[v])
          continue;

        dist[v] = d + w;
        pq.push({dist[v], v});
      }
    }
    dist[src] = INF;
    return count_if(dist.begin(), dist.end(),
                    [thresh](int d) { return d <= thresh; });
  }

public:
  int findTheCity(int n, vector<vector<int>> &edges, int distanceThreshold) {
    vector<vector<pair<int, int>>> adj(n);
    for (const auto &e : edges) {
      adj[e[0]].push_back({e[1], e[2]});
      adj[e[1]].push_back({e[0], e[2]});
    }

    int target = -1, minCount = int(1e9);
    for (int src = 0; src < n; ++src) {
      int count = dijkstra(src, distanceThreshold, n, adj);
      if (count <= minCount) {
        minCount = count;
        target = src;
      }
    }

    return target;
  }
};