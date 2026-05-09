#include <algorithm>
#include <utility>
#include <vector>
using std::vector;

class Solution {
public:
  int dominantIndex(vector<int> &nums) {
    int max1 = nums[0], max2 = nums[1];
    int max1Idx = 0;

    if (max1 < max2) {
      std::swap(max1, max2);
      max1Idx = 1;
    }

    for (int i = 2; i < nums.size(); i++) {
      if (max1 < nums[i]) {
        max2 = max1;
        max1 = nums[i];
        max1Idx = i;
      } else if (max2 < nums[i]) {
        max2 = nums[i];
      }
    }

    if (max1 >= 2 * max2) {
      return max1Idx;
    }

    return -1;
  }
};