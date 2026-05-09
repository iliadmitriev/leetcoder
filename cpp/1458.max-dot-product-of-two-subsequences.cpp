#include <vector>
using std::vector;

class Solution {
public:
  int maxDotProduct(vector<int> &nums1, vector<int> &nums2) {
    // special case 1
    // all positive -> get min
    auto a = std::min_element(nums1.begin(), nums1.end());
    // all negative -> get max
    auto b = std::max_element(nums2.begin(), nums2.end());
    if (*a > 0 && *b < 0) {
      return *a * *b;
    }

    // special case 2
    // all negative -> get max
    auto c = std::max_element(nums1.begin(), nums1.end());
    // all positive -> get min
    auto d = std::min_element(nums2.begin(), nums2.end());
    if (*c < 0 && *d > 0) {
      return *c * *d;
    }

    auto n = nums1.size();
    auto m = nums2.size();

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = n - 1; i >= 0; i--) {
      for (int j = m - 1; j >= 0; j--) {
        dp[i][j] = std::max({nums1[i] * nums2[j] + dp[i + 1][j + 1],
                             dp[i + 1][j], dp[i][j + 1]});
      }
    }

    return dp[0][0];
  }
};