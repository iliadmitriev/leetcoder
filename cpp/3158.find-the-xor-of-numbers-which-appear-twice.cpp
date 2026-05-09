#include <algorithm>
#include <vector>

using std::vector;
class Solution {

public:
  int duplicateNumbersXOR(vector<int> &nums) {

    std::sort(nums.begin(), nums.end());

    int res = 0;

    for (int i = 1; i < nums.size(); ++i) {
      if (nums[i - 1] == nums[i]) {
        res ^= nums[i];
      }
    }

    return res;
  }
};