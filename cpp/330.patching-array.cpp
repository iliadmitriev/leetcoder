#include <vector>

using std::vector;

class Solution {
public:
  int minPatches(vector<int> &nums, int n) {
    int patches = 0, i = 0;
    long cover = 0;

    while (cover < n) {
      if (i < nums.size() && nums[i] <= cover + 1) {
        cover += nums[i++];
      } else {
        cover += cover + 1;
        patches++;
      }
    }

    return patches;
  }
};