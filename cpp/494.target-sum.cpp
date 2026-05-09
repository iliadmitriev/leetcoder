#include <algorithm>
#include <ios>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

using std::vector;

static const int ZERO = []() {
  std::cin.tie(nullptr);
  std::ios_base::sync_with_stdio(false);

  return 0;
}();

class Solution {
public:
  typedef vector<vector<int>> Cache;

  int findTargetSumWays(vector<int> &nums, int target) {
    int shift = std::accumulate(nums.begin(), nums.end(), 0);
    int n = nums.size();

    Cache cache(n + 1, vector<int>(2 * shift + 1, -1));

    int zero =
        std::count_if(nums.begin(), nums.end(),
                      [](const auto &item) -> bool { return item == 0; });

    vector<int> numsNoZeros;
    std::copy_if(nums.begin(), nums.end(), std::back_inserter(numsNoZeros),
                 [](const auto &item) -> bool { return item != 0; });

    return dfs(0, 0, cache, numsNoZeros, target, shift) * (1 << zero);
  }

private:
  int dfs(int i, int value, Cache &cache, const vector<int> &nums,
          const int target, const int shift) {
    if (i == nums.size()) {
      return target == value ? 1 : 0;
    }

    if (cache[i][shift + value] != -1) {
      return cache[i][shift + value];
    }

    return cache[i][shift + value] =
               dfs(i + 1, value + nums[i], cache, nums, target, shift) +
               dfs(i + 1, value - nums[i], cache, nums, target, shift);
  }
};