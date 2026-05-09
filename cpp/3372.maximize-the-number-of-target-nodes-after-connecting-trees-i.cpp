#include <vector>
using std::vector;

class Solution {
private:
  vector<vector<int>> buildAdjacencyList(const vector<vector<int>> &edges) {
    const int n = edges.size() + 1;
    vector<vector<int>> adjList(n);
    for (const auto &edge : edges) {
      adjList[edge[0]].push_back(edge[1]);
      adjList[edge[1]].push_back(edge[0]);
    }
    return adjList;
  }

  int dfs(const vector<vector<int>> &adjList, int node, int parent, int depth) {
    if (depth < 0) {
      return 0;
    }

    int count = 1;
    for (int next : adjList[node]) {
      if (next == parent) {
        continue;
      }
      count += dfs(adjList, next, node, depth - 1);
    }
    return count;
  }

public:
  vector<int> maxTargetNodes(vector<vector<int>> &edges1,
                             vector<vector<int>> &edges2, int k) {
    const vector<vector<int>> adjList1 = buildAdjacencyList(edges1);
    const int n = adjList1.size();

    if (k < 2) {
      vector<int> res(n, 0);
      for (int i = 0; i < n; i++) {
        res[i] = dfs(adjList1, i, -1, k) + k;
      }
      return res;
    }

    const vector<vector<int>> adjList2 = buildAdjacencyList(edges2);
    const int m = adjList2.size();
    int maxNodes2 = 0;

    for (int i = 0; i < m; i++) {
      maxNodes2 = std::max(maxNodes2, dfs(adjList2, i, -1, k - 1));
    }

    vector<int> res(n, 0);
    for (int i = 0; i < n; i++) {
      res[i] = dfs(adjList1, i, -1, k) + maxNodes2;
    }
    return res;
  }
};