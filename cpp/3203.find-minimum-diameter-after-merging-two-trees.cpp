#include <iostream>
#include <utility>
#include <vector>
using std::vector, std::pair, std::max;

static const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  int minimumDiameterAfterMerge(vector<vector<int>> &edges1,
                                vector<vector<int>> &edges2) {

    auto d1 = getMaxDiameter(edges1);
    auto d2 = getMaxDiameter(edges2);

    return max(max(d1, d2), 1 + (d1 / 2 + d1 % 2) + (d2 / 2 + d2 % 2));
  }

private:
  int getMaxDiameter(const vector<vector<int>> &edges) {
    const int k = edges.size();
    vector<vector<int>> adj(k + 1);

    for (const auto &edge : edges) {
      adj[edge[0]].push_back(edge[1]);
      adj[edge[1]].push_back(edge[0]);
    }

    auto [dia, path] = dfsMaxDiameter(0, -1, adj);
    return dia;
  }

  pair<int, int> dfsMaxDiameter(int node, int parent,
                                const vector<vector<int>> &adj) {
    int maxDia = 0, maxPath1 = 0, maxPath2 = 0;

    for (int child : adj[node]) {
      if (child == parent) {
        continue;
      }

      auto [childDia, childPath] = dfsMaxDiameter(child, node, adj);
      maxDia = max(maxDia, childDia);

      if (childPath >= maxPath1) {
        maxPath2 = maxPath1;
        maxPath1 = childPath;
      } else if (childPath > maxPath2) {
        maxPath2 = childPath;
      }
    }

    maxDia = max(maxDia, maxPath1 + maxPath2);

    return {maxDia, 1 + max(maxPath1, maxPath2)};
  }
};