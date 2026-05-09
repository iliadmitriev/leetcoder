#include <vector>
using std::vector;

class Solution {
public:
  int countHillValley(vector<int> &nums) {
    const int n = nums.size();

    int i = 0, j = 1;
    int cnt = 0;

    for (int k = 2; k < n; k++) {
      if (nums[j] == nums[k]) {
        continue;
      }

      if (nums[i] < nums[j] && nums[j] > nums[k]) {
        cnt++;
      } else if (nums[i] > nums[j] && nums[j] < nums[k]) {
        cnt++;
      }

      i = j;
      j = k;
    }

    return cnt;
  }
};