#include <iostream>
#include <numeric>
#include <vector>
using std::vector;

static const int io_sync_off = []() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  int waysToSplitArray(vector<int> &nums) {
    long left = 0, right = std::accumulate(nums.begin(), nums.end(), 0L);
    const int N = nums.size();
    int ans = 0;

    for (int i = 0; i < N - 1; ++i) {
      left += nums[i];
      right -= nums[i];

      if (left >= right) {
        ++ans;
      }
    }

    return ans;
  }
};