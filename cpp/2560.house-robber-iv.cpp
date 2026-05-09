#include <vector>
using std::vector;

class Solution {
public:
  int minCapability(vector<int> &nums, int k) {
    int lo = nums[0], hi = nums[0];
    int mid;

    for (int n : nums) {
      lo = std::min(lo, n);
      hi = std::max(hi, n);
    }

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (checkGTE(nums, k, mid)) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }

private:
  bool checkGTE(const vector<int> &nums, int k, int cap) {
    int prev2 = 0, prev1 = 0, cur = 0;

    for (int n : nums) {
      cur = std::max(prev2 + (n <= cap), prev1);

      if (cur >= k) {
        return true;
      }

      prev2 = prev1;
      prev1 = cur;
    }

    return false;
  }
};