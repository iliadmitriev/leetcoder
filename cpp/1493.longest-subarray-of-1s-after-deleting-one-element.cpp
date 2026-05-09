#include <vector>
using std::vector;

class Solution {
public:
  int longestSubarray(vector<int> &nums) {
    const int n = nums.size();
    int l = 0, longest = 0, zeros = 0;

    for (int r = 0; r < n; r++) {
      if (nums[r] == 0) {
        zeros++;
      }

      while (zeros > 1) {
        if (nums[l] == 0) {
          zeros--;
        }

        l++;
      }

      longest = std::max(longest, r - l); // r - l + 1 - 1 (for deleted zero)
    }

    return longest;
  }
};