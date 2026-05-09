#include <cstdlib>
#include <vector>
using std::vector;

class Solution {
public:
  int maxAbsoluteSum(vector<int> &nums) {
    int maxSum = 0, minSum = 0;
    int curMaxSum = 0, curMinSum = 0;

    for (int num : nums) {
      curMaxSum += num;
      curMinSum += num;

      curMaxSum = std::max(0, curMaxSum);
      curMinSum = std::min(0, curMinSum);

      maxSum = std::max(maxSum, curMaxSum);
      minSum = std::min(minSum, curMinSum);
    }

    return std::max(std::abs(minSum), std::abs(maxSum));
  }
};