#include <cstdlib>
#include <vector>
using std::vector;

class Solution {
public:
  int getMinDistance(vector<int> &nums, int target, int start) {
    int n = nums.size();
    int curMin = n;

    for (int i = start; i < n && std::abs(i - start) < curMin; i++) {
      if (nums[i] == target) {
        curMin = std::abs(i - start);
      }
    }

    for (int i = start; i >= 0 && std::abs(i - start) < curMin; i--) {
      if (nums[i] == target) {
        curMin = std::abs(i - start);
      }
    }

    return curMin;
  }
};