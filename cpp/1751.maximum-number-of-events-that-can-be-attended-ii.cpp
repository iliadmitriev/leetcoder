#include <algorithm>
#include <functional>
#include <vector>
using std::vector;

class Solution {
public:
  int maxValue(vector<vector<int>> &events, int k) {
    const int n = events.size();

    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));

    std::sort(events.begin(), events.end()); // sort by start

    for (int i = n - 1; i >= 0; i--) {
      // find next event that ends before current start
      int idx = bisectRightEnd(events, events[i], i, n,
                               [](const vector<int> &a, const vector<int> &b) {
                                 // one event endis less than next event start
                                 return a[1] < b[0];
                               });

      for (int j = 1; j <= k; j++) {
        dp[i][j] = std::max(dp[i + 1][j], dp[idx][j - 1] + events[i][2]);
      }
    }

    return dp[0][k];
  }

private:
  int bisectRightEnd(
      const vector<vector<int>> &arr, const vector<int> &x, int lo, int hi,
      std::function<bool(const vector<int> &, const vector<int> &)> cmp) {
    int mid;

    while (lo < hi) {
      mid = lo + (hi - lo) / 2;

      if (cmp(x, arr[mid])) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }
};