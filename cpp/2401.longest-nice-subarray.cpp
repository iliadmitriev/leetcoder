#include <vector>
using std::vector;

class Solution {
public:
  int longestNiceSubarray(vector<int> &nums) {
    int mask = 0xffffffff;
    int maxLen = 0;

    int left = 0;

    for (int right = 0; right < nums.size(); right++) {
      mask ^= nums[right];

      while (mask & nums[right]) {
        mask ^= nums[left++];
      }

      maxLen = std::max(maxLen, right - left + 1);
    }

    return maxLen;
  }
};