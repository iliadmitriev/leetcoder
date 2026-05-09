#include <iostream>
#include <vector>

using std::vector;

static const int ZERO = []() {
  std::cin.tie(nullptr);
  std::ios::sync_with_stdio(false);
  return 0;
}();

class Solution {
public:
  int mincostTickets(vector<int> &days, vector<int> &costs) {
    std::sort(days.begin(), days.end());
    const int lastDay = days.back();
    vector<int> dp(lastDay + 1, 0);

    for (int curDay = 1, j = 0; curDay <= lastDay; curDay++) {
      if (curDay < days[j]) {
        // current day is still covered with payment
        dp[curDay] = dp[curDay - 1];
      } else {
        j++;
        dp[curDay] = std::min({
            dp[std::max(0, curDay - 1)] + costs[0],
            dp[std::max(0, curDay - 7)] + costs[1],
            dp[std::max(0, curDay - 30)] + costs[2],
        });
      }
    }

    return dp[lastDay];
  }
};