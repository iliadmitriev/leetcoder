#include <vector>

using std::vector;

class Solution {
public:
  bool check(vector<int> &nums) {
    int prev = nums.front();
    int rotationsLeft = 1;

    // if array is not rotated, all elements must be in order
    // drop all rotations left
    if (nums.front() < nums.back()) {
      rotationsLeft--;
    }

    for (int num : nums) {
      if (num < prev) {
        rotationsLeft--;
      }

      if (rotationsLeft < 0) {
        return false;
      }

      prev = num;
    }

    return true;
  }
};