#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

#include <iostream>
const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  long long maximumSubarraySum(vector<int> &nums, int k) {
    long maxSubSum = 0L;
    long curSum = 0L;
    unordered_map<int, int> window;

    for (int i = 0; i < nums.size(); i++) {
      curSum += nums[i];
      window[nums[i]]++;

      if (i >= k) {
        curSum -= nums[i - k];
        window[nums[i - k]]--;

        if (window[nums[i - k]] == 0) {
          window.erase(nums[i - k]);
        }
      }

      if (i >= k - 1 && window.size() == k) {
        maxSubSum = std::max(maxSubSum, curSum);
      }
    }

    return maxSubSum;
  }
};