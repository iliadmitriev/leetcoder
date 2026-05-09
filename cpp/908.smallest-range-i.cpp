#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
  int smallestRangeI(vector<int> &nums, int k) {
    int minV = *std::min_element(nums.begin(), nums.end()) + k;
    int maxV = *std::max_element(nums.begin(), nums.end()) - k;

    return std::max(0, maxV - minV);
  }
};