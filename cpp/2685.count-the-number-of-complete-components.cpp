#include <numeric>
#include <unordered_map>
#include <utility>
#include <vector>

using std::vector, std::unordered_map;

class UnionFind {
private:
  const int n;
  vector<int> parent, edges, vertices;

public:
  UnionFind(int _n) : n(_n), parent(n), edges(n, 0), vertices(n, 1) {
    std::iota(parent.begin(), parent.end(), 0);
  }

  int find(int x) {
    while (x != parent[x]) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }

    return x;
  }

  void join(int x1, int x2) {
    if (x1 == x2) {
      return;
    }

    int p1 = find(x1), p2 = find(x2);

    if (p1 == p2) {
      edges[p2]++;
      return;
    }

    parent[p1] = p2;
    vertices[p2] += vertices[p1];
    edges[p2] += edges[p1] + 1;
  }

  vector<std::pair<int, int>> get() {
    vector<std::pair<int, int>> result;
    vector<bool> seen(n, false);

    for (int i = 0; i < n; i++) {
      int p = find(i);

      if (seen[p]) {
        continue;
      }

      seen[p] = true;
      result.push_back({vertices[p], edges[p]});
    }

    return result;
  }
};

class Solution {
public:
  int countCompleteComponents(int n, vector<vector<int>> &edges) {
    UnionFind uf(n);

    for (auto &e : edges) {
      uf.join(e[0], e[1]);
    }

    int count = 0;
    for (auto [v, e] : uf.get()) {
      if (e == v * (v - 1) / 2) {
        count++;
      }
    }

    return count;
  }
};