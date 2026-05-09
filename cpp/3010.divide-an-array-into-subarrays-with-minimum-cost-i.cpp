#include <utility>
#include <vector>
using std::vector;

class Solution {
public:
  int minimumCost(vector<int> &nums) {
    int minA = nums[1], minB = nums[2];
    if (minA > minB) {
      std::swap(minA, minB);
    }

    for (int i = 3; i < nums.size(); i++) {
      if (nums[i] < minA) {
        minB = minA;
        minA = nums[i];
      } else if (nums[i] == minA || nums[i] < minB) {
        minB = nums[i];
      }
    }

    return nums[0] + minA + minB;
  }
};