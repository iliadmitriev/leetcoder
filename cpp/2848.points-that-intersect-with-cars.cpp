#include <vector>

using std::vector;

class Solution {
public:
  int numberOfPoints(vector<vector<int>> &nums) {
    std::sort(nums.begin(), nums.end(), [](auto &a, auto &b) -> bool {
      return a[0] < b[0] || (a[0] == b[0] && a[1] < b[1]);
    });

    int holes = 0;
    int minInt = nums[0][0];
    int maxInt = nums[0][1];

    for (int i = 1; i < nums.size(); i++) {
      if (maxInt < nums[i][0]) {
        holes += nums[i][0] - maxInt - 1;
      }

      maxInt = std::max(maxInt, nums[i][1]);
    }

    return maxInt - minInt + 1 - holes;
  }
};