#include <vector>
using std::vector;

class Solution {
public:
  int partitionArray(vector<int> &nums, int k) {
    const int n = nums.size();
    int count = 1;

    std::sort(nums.begin(), nums.end());

    for (int i = 0, j = 0; i < n; i++) {
      if (nums[i] - nums[j] <= k) {
        continue;
      }

      count++;
      j = i;
    }

    return count;
  }
};