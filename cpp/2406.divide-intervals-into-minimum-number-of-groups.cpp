#include <ios>
#include <iostream>
#include <utility>
#include <vector>
using std::vector, std::pair;

class Solution {
public:
  int minGroups(vector<vector<int>> &intervals) {
    int n = intervals.size();
    vector<pair<int, int>> inv;
    inv.reserve(n * 2);

    for (int i = 0; i < n; i++) {
      inv.push_back({intervals[i][0], 1});
      inv.push_back({intervals[i][1] + 1, -1});
    }

    std::sort(inv.begin(), inv.end());

    int curGroups = 0, maxGroups = 0;
    for (auto [_, g] : inv) {
      curGroups += g;
      maxGroups = std::max(maxGroups, curGroups);
    }

    return maxGroups;
  }
};

int init = []() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);
  return 0;
}();
