#include <deque>
#include <numeric>
#include <vector>
using std::vector, std::deque;

class Solution {
private:
  void bfsShortestPath(const vector<vector<int>> &adj, vector<int> &dist,
                       int start) {
    deque<int> q{start};
    int n = dist.size();

    while (q.size()) {
      int node = q.front();
      q.pop_front();
      if (node == n - 1) {
        return;
      }

      for (int child : adj[node]) {
        if (dist[child] <= dist[node] + 1) {
          continue;
        }
        q.push_back(child);
        dist[child] = dist[node] + 1;
      }
    }
  }

public:
  vector<int> shortestDistanceAfterQueries(int n,
                                           vector<vector<int>> &queries) {
    vector<vector<int>> adj(n, vector<int>{});
    for (int i = 0; i < n - 1; i++) {
      adj[i].push_back(i + 1);
    }
    vector<int> dist(n);
    std::iota(dist.begin(), dist.end(), 0);

    int m = queries.size();
    vector<int> answer(m, 0);

    for (int i = 0; i < m; i++) {
      int u = queries[i][0], v = queries[i][1];
      adj[u].push_back(v);

      if (dist[v] >= dist[u] + 1) {
        bfsShortestPath(adj, dist, u);
      }

      answer[i] = dist.back();
    }

    return answer;
  }
};