#include <queue>
#include <vector>
using std::pair;
using std::priority_queue;
using std::vector;

class Solution {
private:
  int INF = int(2e9);

  int dijkstra(const vector<vector<pair<int, int>>> &adj, int source,
               int destination) {
    vector<int> minDist(adj.size(), INF);
    minDist[source] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, std::greater<>> pq;
    pq.push({0, source});

    while (pq.size()) {
      auto [dist, u] = pq.top();
      pq.pop();

      for (auto [v, w] : adj[u]) {
        if (dist + w < minDist[v]) {
          minDist[v] = dist + w;
          pq.push({dist + w, v});
        }
      }
    }

    return minDist[destination];
  }

public:
  vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>> &edges,
                                         int source, int destination,
                                         int target) {

    vector<vector<pair<int, int>>> adj(n);
    for (const auto edge : edges) {
      if (edge[2] == -1)
        continue;

      adj[edge[0]].push_back({edge[1], edge[2]});
      adj[edge[1]].push_back({edge[0], edge[2]});
    }

    int shortestPath = dijkstra(adj, source, destination);
    // if path exists and less than target,
    // we cant build path of length target
    if (shortestPath < target) {
      return {};
    }

    // if current shortest path length is equal to target
    // then nothing to do, we don't need to set any of modifiable edges
    // set all modifiable edges to INF and retrun answer
    if (shortestPath == target) {
      for (auto &edge : edges) {
        if (edge[2] == -1)
          edge[2] = INF;
      }

      return edges;
    }

    // try to set all the modifiable edges to 1, one by one
    // and find if there is a path of length target or less than target
    // if it's less then correct edge weight
    for (int i = 0; i < edges.size(); i++) {
      // skip not modifiable edges
      if (edges[i][2] != -1) {
        continue;
      }

      // set edge weight to 1
      adj[edges[i][0]].push_back({edges[i][1], 1});
      adj[edges[i][1]].push_back({edges[i][0], 1});
      edges[i][2] = 1;
      // find new distance
      int newDistance = dijkstra(adj, source, destination);
      // if there is a path of length target or less than target
      if (newDistance <= target) {
        edges[i][2] += target - newDistance;

        for (int j = i + 1; j < edges.size(); j++) {
          if (edges[j][2] == -1) {
            edges[j][2] = INF;
          }
        }

        return edges;
      }
    }

    return {};
  }
};