#include <vector>

using std::vector;

class Solution {
public:
  int findNonMinOrMax(vector<int> &nums) {
    int maxItem = nums[0], minItem = nums[0];

    for (int i = 1; i < nums.size(); ++i) {
      if (nums[i] > maxItem) {
        maxItem = nums[i];
      } else if (nums[i] < minItem) {
        minItem = nums[i];
      }
    }

    for (int num : nums) {
      if (minItem < num && num < maxItem) {
        return num;
      }
    }

    return -1;
  }
};