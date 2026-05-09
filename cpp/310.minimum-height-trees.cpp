#include <numeric>
#include <queue>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges) {
    if (n <= 2) {
      vector<int> v(n);
      iota(v.begin(), v.end(), 0);
      return v;
    }

    vector<set<int>> graph(n);
    for (auto &e : edges) {
      graph[e[0]].insert(e[1]);
      graph[e[1]].insert(e[0]);
    }

    queue<int> leaves;
    for (int i = 0; i < n; i++) {
      if (graph[i].size() == 1) {
        leaves.push(i);
      }
    }

    while (n > 2) {
      n -= leaves.size();

      for (int l = leaves.size(); l > 0; l--) {
        int leaf = leaves.front();
        leaves.pop();

        for (int child : graph[leaf]) {
          graph[child].erase(leaf);
          if (graph[child].size() == 1) {
            leaves.push(child);
          }
        }
      }
    }

    vector<int> res;
    while (leaves.size()) {
      res.push_back(leaves.front());
      leaves.pop();
    }
    return res;
  }
};