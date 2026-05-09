#include <tuple>
#include <unordered_map>
#include <vector>

using std::tuple;
using std::unordered_map;
using std::vector;
class Solution {
public:
  int findShortestSubArray(vector<int> &nums) {
    unordered_map<int, tuple<int, int, int>> m; // num -> start, end, count
    int degree = 1, n = nums.size(), res = nums.size();

    for (int i = 0; i < n; i++) {
      if (m.find(nums[i]) != m.end()) {
        auto [start, _, count] = m[nums[i]];
        m[nums[i]] = {start, i, count + 1};
        degree = std::max(degree, count + 1);
      } else {
        m[nums[i]] = {i, i, 1};
      }
    }

    for (auto [k, v] : m) {
      auto [start, end, count] = v;
      if (count == degree)
        res = std::min(res, end - start + 1);
    }

    return res;
  }
};