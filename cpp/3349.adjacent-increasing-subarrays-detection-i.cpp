#include <vector>
using std::vector;

class Solution {
public:
  bool hasIncreasingSubarrays(vector<int> &nums, int k) {
    const int n = nums.size();
    int cur = 1, prev = 0;

    for (int i = 1; i < n; i++) {
      if (nums[i - 1] < nums[i]) {
        cur++;
      } else {

        prev = cur;
        cur = 1;
      }

      if ((cur >= k && prev >= k) || (cur >= 2 * k)) {
        return true;
      }
    }

    return false;
  }
};