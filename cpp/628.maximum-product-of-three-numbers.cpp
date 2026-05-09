#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
  int maximumProduct(vector<int> &nums) {
    std::sort(nums.begin(), nums.begin() + 3);

    int max1, max2, max3;
    max1 = nums[2];
    max2 = nums[1];
    max3 = nums[0];

    int min1, min2;
    min1 = nums[0];
    min2 = nums[1];

    for (vector<int>::iterator it = nums.begin() + 3; it != nums.end(); it++) {
      int n = *it;

      if (n > max1) {
        max3 = max2;
        max2 = max1;
        max1 = n;
      } else if (n > max2) {
        max3 = max2;
        max2 = n;
      } else if (n > max3) {
        max3 = n;
      }

      if (n < min1) {
        min2 = min1;
        min1 = n;
      } else if (n < min2) {
        min2 = n;
      }
    }

    return std::max(min1 * min2 * max1, max1 * max2 * max3);
  }
};