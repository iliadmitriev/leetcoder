#include <ios>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>
using std::vector, std::pair, std::priority_queue;

static const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  vector<int> leftmostBuildingQueries(vector<int> &heights,
                                      vector<vector<int>> &queries) {
    const int n = heights.size();
    vector<vector<pair<int, int>>> data(n);

    const int m = queries.size();
    vector<int> result(m, -1);

    for (int i = 0; i < m; i++) {
      int left = queries[i][0], right = queries[i][1];
      if (left > right) {
        std::swap(left, right);
      }

      if (left == right || heights[left] < heights[right]) {
        result[i] = right;
        continue;
      }

      int bothHeight = std::max(heights[left], heights[right]);
      data[right].push_back({bothHeight, i});
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, std::greater<>> pq;

    for (int i = 0; i < n; i++) {
      for (auto &v : data[i]) {
        pq.push(v);
      }

      while (!pq.empty() && pq.top().first < heights[i]) {
        int idx = pq.top().second;
        result[idx] = i;
        pq.pop();
      }
    }

    return result;
  }
};