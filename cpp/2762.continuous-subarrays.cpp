#include <cstdlib>
#include <functional>
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
  long long continuousSubarrays(vector<int> &nums) {
    long long count = 0;

    auto cmp = [](const pair<int, int> &a, const pair<int, int> &b) -> bool {
      if (a.first != b.first) {
        return a.first < b.first;
      }

      return a.second > b.second;
    };

    priority_queue<pair<int, int>, vector<pair<int, int>>, std::greater<>> minQ;
    priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> maxQ;

    const int n = nums.size();

    for (int left = -1, right = 0; right < n; right++) {

      while (!minQ.empty() && std::abs(minQ.top().first - nums[right]) > 2) {
        left = minQ.top().second;
        minQ.pop();
      }

      while (!maxQ.empty() && std::abs(maxQ.top().first - nums[right]) > 2) {
        left = maxQ.top().second;
        maxQ.pop();
      }

      minQ.push({nums[right], right});
      maxQ.push({nums[right], right});
      count += right - left;
    }

    return count;
  }
};