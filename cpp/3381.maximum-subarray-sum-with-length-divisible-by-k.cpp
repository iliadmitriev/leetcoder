#include <vector>
using std::vector;

class Solution {
public:
  long long maxSubarraySum(vector<int> &nums, int k) {
    typedef long long ll;
    const ll inf = 1e15;

    const int n = nums.size();
    ll res = -inf;
    ll prev = 0, cur = 0;
    vector<ll> mins(k, inf);
    mins.back() = 0;

    for (int i = 0; i < n; i++) {
      cur += nums[i];
      prev = mins[i % k];
      mins[i % k] = std::min(prev, cur);
      res = std::max(res, cur - prev);
    }

    return res;
  }
};