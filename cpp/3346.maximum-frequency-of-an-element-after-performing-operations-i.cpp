#include <algorithm>
#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
public:
  int maxFrequency(vector<int> &nums, int k, int numOperations) {
    const int n = nums.size();
    const int maxNum = *std::max_element(nums.begin(), nums.end());
    vector<int> freq(maxNum + 1, 0);
    // unordered_map<int, int> freq;

    for (int num : nums) {
      freq[num]++;
    }

    // left: [num - k, num - 1]
    // right [num + 1, num + k]
    int left = 0, right = 0;
    int maxFreq = 0;
    int limit = std::min(k, maxNum + 1);

    for (int i = 0; i < limit; i++) {
      right += freq[i];
    }

    for (int num = 0; num <= maxNum; num++) {
      right -= freq[num];

      if (num + k <= maxNum) {
        right += freq[num + k];
      }

      if (num - 1 >= 0) {
        left += freq[num - 1];
      }

      if (num - k - 1 >= 0) {
        left -= freq[num - k - 1];
      }

      maxFreq =
          std::max(maxFreq, freq[num] + std::min(numOperations, right + left));
    }

    return maxFreq;
  }
};