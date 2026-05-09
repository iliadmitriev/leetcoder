#include <vector>

using std::vector;

class Solution {
public:
  int minKBitFlips(vector<int> &nums, int k) {
    int flips = 0, n = nums.size(), inv = 0;
    vector<bool> flipped(n, false);

    for (int i = 0; i < n; i++) {
      if (i >= k && flipped[i - k]) {
        inv = 1 - inv;
      }

      if (inv == nums[i]) {
        if (i + k > n) {
          return -1;
        }

        flips++;
        flipped[i] = true;
        inv = 1 - inv;
      }
    }

    return flips;
  }
};