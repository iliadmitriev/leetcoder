#include <vector>

using std::vector;

class Solution {
private:
  void dfs(const vector<vector<int>> &adj, int node, int start,
           vector<vector<int>> &ancestors) {
    for (auto child : adj.at(node)) {
      // check if node `start` is already added to node `child` list
      // from different path
      if (ancestors[child].empty() || ancestors[child].back() != start) {
        ancestors[child].push_back(start);
        dfs(adj, child, start, ancestors);
      }
    }
  }

public:
  vector<vector<int>> getAncestors(int n, vector<vector<int>> &edges) {
    vector<vector<int>> ancestors(n);
    vector<vector<int>> adjList(n);

    for (const auto &edge : edges) {
      adjList[edge[0]].push_back(edge[1]);
    }

    for (int start = 0; start < n; start++) {
      dfs(adjList, start, start, ancestors);
    }

    return ancestors;
  }
};