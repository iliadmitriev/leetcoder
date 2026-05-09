#include <vector>

using std::vector;

class Solution {
public:
  int returnToBoundaryCount(vector<int> &nums) {
    int ans = 0;
    for (int i = 1; i < nums.size(); ++i) {
      nums[i] += nums[i - 1];
      ans += nums[i] == 0;
    }

    return ans;
  }
};