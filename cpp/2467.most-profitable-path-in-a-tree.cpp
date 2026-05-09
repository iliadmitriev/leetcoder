#include <deque>
#include <vector>

using std::vector, std::deque, std::pair;

class Solution {
public:
  int mostProfitablePath(vector<vector<int>> &edges, int bob,
                         vector<int> &amount) {
    const int NEG_INF = std::numeric_limits<int>::min();
    const int n = amount.size();
    vector<vector<int>> tree(n), adj(n);
    deque<pair<int, int>> q, q1;
    vector<int> parent(n);
    int profit = NEG_INF;

    for (const auto &e : edges) {
      tree[e[0]].push_back(e[1]);
      tree[e[1]].push_back(e[0]);
    }

    q1.push_back({0, 0}); // node, parent node
    while (q1.size()) {
      auto [u, p] = q1.front();
      q1.pop_front();

      parent[u] = p;

      for (int v : tree[u]) {
        if (v == p) {
          continue;
        }

        adj[u].push_back(v);
        q1.push_back({v, u});
      }
    }

    q.push_back({0, 0}); // current cost, node
    while (q.size()) {
      for (int m = q.size(); m; m--) {
        auto [cost, alice] = q.front();
        q.pop_front();

        int curProfit = amount[alice];
        if (alice == bob) {
          curProfit /= 2;
        }

        if (!adj[alice].size()) {
          profit = std::max(profit, cost + curProfit);
        }

        for (auto next : adj[alice]) {
          q.push_back({cost + curProfit, next});
        }
      }

      amount[bob] = 0;
      bob = parent[bob];
    }

    return profit;
  }
};