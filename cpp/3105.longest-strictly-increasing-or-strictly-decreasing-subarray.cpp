#include <vector>

using std::vector;

class Solution {
public:
  int longestMonotonicSubarray(vector<int> &nums) {
    const int N = nums.size();
    int inc = 1, dec = 1;
    int longest = 1;

    for (int i = 1; i < N; i++) {
      if (nums[i - 1] < nums[i]) {
        inc++;
        dec = 1;
      } else if (nums[i - 1] > nums[i]) {
        dec++;
        inc = 1;
      } else {
        inc = 1;
        dec = 1;
      }

      longest = std::max(longest, inc);
      longest = std::max(longest, dec);
    }
    return longest;
  }
};