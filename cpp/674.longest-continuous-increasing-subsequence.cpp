#include <vector>
using std::vector;

class Solution {
public:
  int findLengthOfLCIS(vector<int> &nums) {
    int res = 1, len = 1, n = nums.size();

    for (int i = 1; i < n; i++) {
      if (nums[i - 1] < nums[i]) {
        len++;
      } else {
        len = 1;
      }

      res = std::max(res, len);
    }

    return res;
  }
};