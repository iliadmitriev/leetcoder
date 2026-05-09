#include <numeric>
#include <vector>

using std::vector, std::accumulate;

class Solution {
public:
  int countPartitions(vector<int> &nums) {
    const int n = nums.size();
    int left = 0, right = accumulate(nums.begin(), nums.end(), 0);
    int count = 0;

    for (int i = 0; i < n - 1; i++) {
      left += nums[i];
      right -= nums[i];

      if ((left - right) % 2 == 0) {
        count++;
      }
    }

    return count;
  }
};