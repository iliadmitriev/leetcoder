#include <vector>
using std::vector;

class Solution {
public:
  int maxKDivisibleComponents(int n, vector<vector<int>> &edges,
                              vector<int> &values, int k) {
    vector<vector<int>> adj(n);

    for (const auto &edge : edges) {
      adj[edge[0]].push_back(edge[1]);
      adj[edge[1]].push_back(edge[0]);
    }

    return dfsMaxComp(0, -1, k, adj, values).first;
  }

private:
  std::pair<int, long> dfsMaxComp(int node, int parent, int k,
                                  const vector<vector<int>> &adj,
                                  const vector<int> &values) {
    int maxComp = 0;
    long total = values[node];

    for (int child : adj[node]) {
      if (child == parent)
        continue;

      auto [cmp, add] = dfsMaxComp(child, node, k, adj, values);
      total += add;
      maxComp += cmp;
    }

    maxComp += (total % k == 0);

    return {maxComp, total};
  }
};