#include <vector>
using std::vector;

class Solution {
public:
  int maxIncreasingSubarrays(vector<int> &nums) {
    const int n = nums.size();

    int cur = 1, prev = 0;
    int maxLen = 0;

    for (int i = 1; i < n; i++) {
      if (nums[i - 1] < nums[i]) {
        cur++;
      } else {
        prev = cur;
        cur = 1;
      }

      maxLen = std::max(maxLen, std::min(cur, prev));
      maxLen = std::max(maxLen, cur / 2);
    }

    return maxLen;
  }
};