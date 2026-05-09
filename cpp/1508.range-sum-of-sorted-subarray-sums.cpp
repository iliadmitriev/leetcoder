#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
  int rangeSum(vector<int> &nums, int n, int left, int right) {
    vector<int> subs;
    subs.reserve(n);

    for (int start = 0; start < n; ++start) {
      int sum = 0;
      for (int i = start; i < n; ++i) {
        sum += nums[i];
        subs.push_back(sum);
      }
    }

    std::sort(subs.begin(), subs.end());

    int result = 0;
    for (int i = left - 1; i < right; ++i) {
      result = (result + subs[i]) % 1000000007;
    }

    return result;
  }
};