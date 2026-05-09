#include <vector>

using std::vector;

class Solution {
public:
  int minOperations(vector<int> &nums) {
    int ops = 0;
    int value = nums[0];

    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] > value) {
        value = nums[i];
      } else {
        value++;
        ops += value - nums[i];
      }
    }

    return ops;
  }
};