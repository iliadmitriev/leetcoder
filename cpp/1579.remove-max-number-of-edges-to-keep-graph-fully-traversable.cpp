#include <numeric>
#include <tuple>
#include <unordered_set>
#include <utility>
#include <vector>

using std::iota;
using std::swap;
using std::tuple;
using std::unordered_set;
using std::vector;

class DSU {
private:
  int size;
  vector<int> parent;
  vector<int> rank;

public:
  DSU(int _size) : size(_size), parent(_size, 0), rank(_size, 1) {
    iota(parent.begin(), parent.end(), 0);
  }

  int find(int x) {
    while (x != parent[x]) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  }

  bool join(int x, int y) {
    int par_x = find(x);
    int par_y = find(y);

    if (par_x == par_y) {
      return false;
    }

    if (rank[par_x] < rank[par_y]) {
      swap(par_x, par_y);
    }

    parent[par_y] = par_x;
    rank[par_x] += rank[par_y];
    rank[par_y] = 0;
    return true;
  }

  int count() {
    vector<int> cache(size, 0);
    int res = 0;
    for (int i = 0; i < size; i++) {
      int par = find(i);
      res += 1 - cache[par];
      cache[par] = 1;
    }
    return res;
  }
};

class Solution {
public:
  int maxNumEdgesToRemove(int n, vector<vector<int>> &edges) {
    vector<tuple<int, int>> bob, alice, both;
    // add split edges, to 3 vectors of tuples
    // shift vector numeration to start from 0
    for (const auto edge : edges) {
      if (edge[0] == 1) {
        // Alice
        alice.push_back({edge[1] - 1, edge[2] - 1});
      } else if (edge[0] == 2) {
        // Bob
        bob.push_back({edge[1] - 1, edge[2] - 1});
      } else {
        // both
        both.push_back({edge[1] - 1, edge[2] - 1});
      }
    }

    int counter = 0;
    DSU bob_dsu = DSU(n), alice_dsu = DSU(n);

    for (const auto [from, to] : both) {
      bool res1 = bob_dsu.join(from, to);
      bool res2 = alice_dsu.join(from, to);
      if (!res1 || !res2) {
        counter++;
      }
    }

    for (const auto [from, to] : alice) {
      if (!alice_dsu.join(from, to)) {
        counter++;
      }
    }

    for (const auto [from, to] : bob) {
      if (!bob_dsu.join(from, to)) {
        counter++;
      }
    }
    return bob_dsu.count() == 1 && alice_dsu.count() == 1 ? counter : -1;
  }
};