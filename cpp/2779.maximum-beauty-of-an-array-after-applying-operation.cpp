#include <algorithm>
#include <iostream>
#include <vector>
using std::vector;

const static int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  int maximumBeauty(vector<int> &nums, int k) {
    std::sort(nums.begin(), nums.end());

    int maxLen = 0;
    int left = 0;

    for (int right = 0; right < nums.size(); right++) {
      while (nums[right] - nums[left] > 2 * k) {
        left++;
      }

      maxLen = std::max(maxLen, right - left + 1);
    }

    return maxLen;
  }
};