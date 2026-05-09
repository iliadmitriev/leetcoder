#include <algorithm>
#include <vector>
using std::vector;

class Solution {
public:
  vector<int> largestDivisibleSubset(vector<int> &nums) {
    const int n = nums.size();
    vector<int> dp(n, 1), chain(n, -1);
    int idx = 0;

    std::sort(nums.begin(), nums.end());
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < i; j++) {
        if (nums[i] % nums[j] == 0) {
          if (dp[i] < dp[j] + 1) {
            dp[i] = dp[j] + 1;
            chain[i] = j;
          }
        }
      }
      if (dp[i] > dp[idx]) {
        idx = i;
      }
    }

    vector<int> res(dp[idx]);
    int i = 0;
    while (idx != -1) {
      res[i++] = nums[idx];
      idx = chain[idx];
    }

    return res;
  }
};