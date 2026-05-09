#include <vector>
using std::vector;

class Solution {
public:
  int countSubarrays(vector<int> &nums) {
    const int n = nums.size();
    int total = 0;

    for (int i = 1; i < n - 1; i++) {
      if (2 * (nums[i - 1] + nums[i + 1]) == nums[i]) {
        total++;
      }
    }

    return total;
  }
};