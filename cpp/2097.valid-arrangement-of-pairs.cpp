#include <ios>
#include <iostream>
#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  vector<vector<int>> validArrangement(vector<vector<int>> &pairs) {
    unordered_map<int, vector<int>> adj;
    unordered_map<int, int> degree;

    for (vector<int> &pair : pairs) {
      adj[pair[0]].push_back(pair[1]);
      degree[pair[0]]--;
      degree[pair[1]]++;
    }

    int start = pairs[0][0];
    for (auto &[node, deg] : degree) {
      if (deg == -1) {
        start = node;
        break;
      }
    }

    vector<int> stack = {start};
    int cur = start;
    vector<int> path;

    while (stack.size()) {
      if (adj[cur].size()) {
        stack.push_back(cur);
        auto next = adj[cur].back();
        adj[cur].pop_back();
        cur = next;
      } else {
        path.push_back(cur);
        cur = stack.back();
        stack.pop_back();
      }
    }

    vector<vector<int>> res;
    for (int i = path.size() - 2; i >= 0; i--) {
      res.push_back({path[i + 1], path[i]});
    }

    return res;
  }
};