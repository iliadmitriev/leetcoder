#include <vector>

using std::vector;

class Solution {
public:
  int findKOr(vector<int> &nums, int k) {
    int res = 0;

    for (int i = 0; i < 32; i++) {
      int counter = 0;
      for (int j = 0; j < nums.size(); j++) {
        if ((nums[j] >> i) & 1) {
          counter++;
        }

        if (counter >= k) {
          res |= (1 << i);
          break;
        }
      }
    }

    return res;
  }
};