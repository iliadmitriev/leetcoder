#include <numeric>
#include <vector>

using std::vector;

class UnionFind {
private:
  vector<int> parent;

public:
  UnionFind(int size) : parent(size) {
    std::iota(parent.begin(), parent.end(), 0);
  }

  int find(int x) {
    while (x != parent[x]) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return parent[x];
  }

  bool join(int x, int y) {
    int parX = find(x), parY = find(y);
    if (parX == parY) {
      return false;
    }

    parent[parX] = parY;
    return true;
  }
};

class Solution {
public:
  vector<int> findRedundantConnection(vector<vector<int>> &edges) {
    const int N = edges.size();
    UnionFind uf(N + 1);

    for (const auto &edge : edges) {
      int u = edge[0], v = edge[1];
      if (!uf.join(u, v)) {
        return edge;
      }
    }

    return {};
  }
};