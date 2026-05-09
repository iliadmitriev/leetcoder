#include <vector>
using std::vector;

class Solution {
public:
  long long maximumTripletValue(vector<int> &nums) {
    long result = 0;
    const int n = nums.size();
    vector<int> prefix(n, 0), suffix(n, 0);

    int cur = nums[0];
    for (int i = 0; i < n; i++) {
      cur = std::max(cur, nums[i]);
      prefix[i] = cur;
    }

    cur = nums[n - 1];
    for (int i = n - 1; i >= 0; i--) {
      cur = std::max(cur, nums[i]);
      suffix[i] = cur;
    }

    for (int i = 1; i < n - 1; i++) {
      result = std::max(result, 1L * (prefix[i - 1] - nums[i]) * suffix[i + 1]);
    }

    return result;
  }
};