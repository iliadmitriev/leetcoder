#include <vector>
using std::vector;

class Solution {
public:
  long long countSubarrays(vector<int> &nums, int k) {
    const int n = nums.size();
    const int max = *std::max_element(nums.begin(), nums.end());
    long long total = 0;
    int count = 0;

    for (int i = 0, j = 0; i < n; i++) {
      count += nums[i] == max;

      while (count >= k) {
        count -= nums[j++] == max;
      }

      total += j;
    }

    return total;
  }
};