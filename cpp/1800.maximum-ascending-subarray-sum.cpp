#include <vector>
using std::vector;

class Solution {
public:
  int maxAscendingSum(vector<int> &nums) {
    int currSum = 0, maxSum = 0;
    int prev = 0;

    for (int num : nums) {
      if (prev < num) {
        currSum += num;
      } else {
        currSum = num;
      }

      prev = num;

      maxSum = std::max(maxSum, currSum);
    }

    return maxSum;
  }
};