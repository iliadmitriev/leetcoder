#include <algorithm>
#include <vector>
using std::vector;

#include <iostream>
const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  int minimumSubarrayLength(vector<int> &nums, int k) {
    if (k == 0) {
      return 1;
    }

    const int n = nums.size();
    const int maxBits = int(std::log2(std::max(
                            k, *std::max_element(nums.begin(), nums.end())))) +
                        1;

    int left = 0;
    int cur = 0;
    int minLen = n + 1;
    vector<int> bitCount(maxBits, 0);

    for (int right = 0; right < n; right++) {
      int num = nums[right];
      cur |= num;
      for (int j = 0; num > 0; j++) {
        bitCount[j] += num & 1;
        num >>= 1;
      }

      while (left < n && cur >= k) {
        minLen = std::min(minLen, right - left + 1);

        int num = nums[left];
        for (int j = 0; num > 0; j++) {
          bitCount[j] -= num & 1;
          // reset j-th bit of current value if it's count is 0.
          cur &= ~((bitCount[j] == 0) << j);
          num >>= 1;
        }
        left++;
      }
    }

    if (minLen > n) {
      return -1;
    }

    return minLen;
  }
};