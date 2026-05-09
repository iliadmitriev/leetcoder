#include <algorithm>
#include <limits>
#include <vector>
using std::vector;

class Solution {
public:
  int maxSubArray(vector<int> &nums) {
    int maxSum = std::numeric_limits<int>::min();
    int curSum = 0;

    for (int num : nums) {
      curSum += num;
      maxSum = std::max(maxSum, curSum);
      curSum = std::max(0, curSum);
    }

    return maxSum;
  }
};