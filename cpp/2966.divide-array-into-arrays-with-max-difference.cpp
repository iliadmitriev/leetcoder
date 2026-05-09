#include <vector>
using std::vector;

class Solution {
public:
  vector<vector<int>> divideArray(vector<int> &nums, int k) {
    const size_t n = nums.size();

    std::sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    res.reserve(n / 3);

    for (int i = 0; i < n; i += 3) {
      if (nums[i + 2] - nums[i] > k) {
        return {};
      }

      res.push_back({nums[i], nums[i + 1], nums[i + 2]});
    }

    return res;
  }
};