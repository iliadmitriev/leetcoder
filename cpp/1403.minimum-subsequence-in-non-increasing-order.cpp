#include <algorithm>
#include <numeric>
#include <vector>

using std::vector;

class Solution {
public:
  vector<int> minSubsequence(vector<int> &nums) {
    std::sort(nums.rbegin(), nums.rend());
    int total = std::accumulate(nums.begin(), nums.end(), 0);

    int acc = 0;

    for (int i = 0; i < nums.size(); i++) {
      acc += nums[i];

      if (2 * acc > total) {
        return vector<int>(nums.begin(), nums.begin() + i + 1);
      }
    }

    return nums;
  }
};