#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
  bool validPath(int n, vector<vector<int>> &edges, int source,
                 int destination) {
    vector<vector<int>> adj(n, vector<int>(0));

    for (auto &edge : edges) {
      adj[edge[0]].push_back(edge[1]);
      adj[edge[1]].push_back(edge[0]);
    }

    queue<int> q;
    vector<bool> visited(n, false);

    q.push(source);
    visited[source] = true;

    while (!q.empty()) {
      int node = q.front();
      q.pop();

      if (node == destination)
        return true;

      for (int next : adj[node]) {
        if (!visited[next]) {
          q.push(next);
          visited[next] = true;
        }
      }
    }
    return false;
  }
};