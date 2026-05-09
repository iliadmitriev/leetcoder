#include <functional>
#include <iostream>
#include <numeric>
#include <queue>
#include <utility>
#include <vector>

using std::vector, std::priority_queue, std::pair;

static const auto fast = []() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return nullptr;
}();

class Solution {
public:
  double maxAverageRatio(vector<vector<int>> &classes, int extraStudents) {
    const int n = classes.size();
    priority_queue<pair<double, int>, vector<pair<double, int>>, std::less<>>
        hq;

    for (int i = 0; i < n; i++) {
      if (classes[i][0] > classes[i][1]) {
        continue;
      }

      hq.push({extra(classes[i][0], classes[i][1]), i});
    }

    while (extraStudents-- && hq.size()) {
      int i = hq.top().second;
      hq.pop();

      classes[i][0]++;
      classes[i][1]++;

      hq.push({extra(classes[i][0], classes[i][1]), i});
    }

    return std::accumulate(classes.begin(), classes.end(), 0.0,
                           [&](double p, const auto &c) {
                             return p + double(c[0]) / c[1];
                           }) /
           n;
  }

private:
  inline double extra(int count, int total) {
    return (count + 1.0) / (total + 1.0) - double(count) / total;
  }
};