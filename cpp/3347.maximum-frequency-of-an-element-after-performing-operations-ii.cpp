#include <algorithm>
#include <unordered_map>
#include <vector>
using std::vector, std::unordered_map;

class Solution {
public:
  int maxFrequency(vector<int> &nums, int k, int numOperations) {
    std::sort(nums.begin(), nums.end());

    unordered_map<int, int> cnt;
    for (int num : nums) {
      cnt[num]++;
    }

    int left, right, maxFreq = 0;
    int candidate1, candidate2, window1, window2;

    for (int i = 0; i < nums.size(); i++) {
      left = std::lower_bound(nums.begin(), nums.end(), nums[i] - k) -
             nums.begin();
      right = std::upper_bound(nums.begin(), nums.end(), nums[i] + k) -
              nums.begin();

      window1 = right - left - cnt[nums[i]];
      candidate1 = cnt[nums[i]] + std::min(window1, numOperations);
      maxFreq = std::max(maxFreq, candidate1);

      window2 =
          std::upper_bound(nums.begin(), nums.end(), 1LL * nums[i] + 2 * k) -
          nums.begin() - i;
      candidate2 = std::min(window2, numOperations);
      maxFreq = std::max(maxFreq, candidate2);
    }

    return maxFreq;
  }
};