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

  int dfs(const vector<vector<int>> &adjList, int node, int parent,
          bool even = true) {
    int count = 0;

    if (even) {
      count++;
    }

    for (int next : adjList[node]) {
      if (next == parent) {
        continue;
      }
      count += dfs(adjList, next, node, !even);
    }
    return count;
  }

  void dfsEven(const vector<vector<int>> &adjList, const vector<int> &counts,
               vector<int> &res, int node, int parent, int even = 0) {
    res[node] = counts[even];

    for (int next : adjList[node]) {
      if (next == parent) {
        continue;
      }
      dfsEven(adjList, counts, res, next, node, 1 - even);
    }
  }

public:
  vector<int> maxTargetNodes(vector<vector<int>> &edges1,
                             vector<vector<int>> &edges2) {
    const vector<vector<int>> adjList1 = buildAdjacencyList(edges1);
    const int n = adjList1.size();

    const vector<vector<int>> adjList2 = buildAdjacencyList(edges2);
    const int m = adjList2.size();

    const int even1 = dfs(adjList1, 0, -1);
    const int even2 = dfs(adjList2, 0, -1);
    const int odd1 = n - even1;
    const int odd2 = m - even2;

    const int maxNodes2 = std::max(even2, odd2);
    const vector<int> counts({even1 + maxNodes2, odd1 + maxNodes2});

    vector<int> res(n, 0);
    dfsEven(adjList1, counts, res, 0, -1);

    return res;
  }
};