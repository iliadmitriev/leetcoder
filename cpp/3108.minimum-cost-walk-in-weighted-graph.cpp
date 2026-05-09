#include <numeric>
#include <vector>
using std::vector;

class UnionFind {
private:
  vector<int> parent, weight;

public:
  UnionFind(int n) : parent(n), weight(n, -1) {
    std::iota(parent.begin(), parent.end(), 0);
  }

  std::pair<int, int> find(int x) {
    while (x != parent[x]) {
      weight[x] &= weight[parent[x]];
      weight[parent[x]] &= weight[x];

      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return {x, weight[x]};
  }

  void join(int x1, int x2, int w) {
    auto [p1, w1] = find(x1);
    auto [p2, w2] = find(x2);

    w &= w1 & w2;

    parent[p1] = p2;
    weight[p1] = w;
    weight[p2] = w;
  }
};

class Solution {
public:
  vector<int> minimumCost(int n, vector<vector<int>> &edges,
                          vector<vector<int>> &query) {
    UnionFind uf(n);
    vector<int> ans(query.size(), -1);

    for (int i = 0; i < edges.size(); i++) {
      uf.join(edges[i][0], edges[i][1], edges[i][2]);
    }

    for (int i = 0; i < query.size(); i++) {
      if (query[i][0] == query[i][1]) {
        continue;
      }

      auto [p1, w1] = uf.find(query[i][0]);
      auto [p2, w2] = uf.find(query[i][1]);

      if (p1 != p2) {
        continue;
      }

      ans[i] = w1 & w2;
    }

    return ans;
  }
};