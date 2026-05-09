#include <algorithm>
#include <vector>

using std::sort;
using std::vector;

class Solution {
public:
  int arrayPairSum(vector<int> &nums) {
    int total = 0, n = nums.size();
    sort(nums.begin(), nums.end());

    for (int i = 0; i < n; i += 2) {
      total += nums[i];
    }

    return total;
  }
};