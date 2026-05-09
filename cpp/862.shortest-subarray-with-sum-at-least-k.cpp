#include <utility>
#include <vector>

#include <iostream>
const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

using std::vector, std::deque, std::pair;
typedef long agg_t;
typedef pair<agg_t, int> item;

class Solution {
public:
  int shortestSubarray(vector<int> &nums, int k) {
    int res = nums.size() + 1;

    deque<item> q({{0L, -1}});
    agg_t cur = 0;

    for (int i = 0; i < nums.size(); i++) {
      cur += nums[i];

      while (q.size() && q.back().first >= cur) {
        q.pop_back();
      }

      q.push_back({cur, i});

      while (q.size() && cur - q.front().first >= k) {
        res = std::min(res, i - q.front().second);
        q.pop_front();
      }
    }

    if (res > nums.size()) {
      return -1;
    }
    return res;
  }
};