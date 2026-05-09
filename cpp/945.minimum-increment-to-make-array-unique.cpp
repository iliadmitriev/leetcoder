#include <algorithm>
#include <vector>

using std::sort;
using std::vector;

class Solution {
public:
  int minIncrementForUnique(vector<int> &nums) {
    int prev = -1;
    int ans = 0;
    sort(nums.begin(), nums.end());

    for (int i = 0; i < nums.size(); ++i) {
      if (prev < nums[i]) {
        prev = nums[i];
        continue;
      }

      ans += prev - nums[i] + 1;
      prev = prev + 1;
    }

    return ans;
  }
};