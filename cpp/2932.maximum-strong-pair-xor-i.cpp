#include <vector>
using std::vector;

class Solution {
public:
  int maximumStrongPairXor(vector<int> &nums) {
    int res = 0;
    std::sort(nums.begin(), nums.end());

    int n = nums.size();

    for (int i = 0; i < n - 1; ++i) {
      for (int j = i + 1; j < n; ++j) {
        if (nums[j] > 2 * nums[i]) {
          break;
        }

        res = std::max(res, nums[i] ^ nums[j]);
      }
    }

    return res;
  }
};