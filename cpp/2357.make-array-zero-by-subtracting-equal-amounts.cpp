#include <vector>

using std::vector;

class Solution {
public:
  int minimumOperations(vector<int> &nums) {
    int ops = 0, shift = 0;

    std::sort(nums.begin(), nums.end());

    for (int num : nums) {
      if (num - shift > 0) {
        shift = num;
        ops += 1;
      }
    }

    return ops;
  }
};