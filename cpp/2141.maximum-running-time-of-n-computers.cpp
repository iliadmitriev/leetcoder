#include <algorithm>
#include <numeric>
#include <vector>

using std::vector;

class Solution {
public:
  long long maxRunTime(int n, vector<int> &batteries) {
    auto m = batteries.size();
    std::sort(batteries.begin(), batteries.end());

    auto extra = std::reduce(batteries.begin(), batteries.end() - n, long());

    std::vector<int> live;
    live.assign(batteries.end() - n, batteries.end());

    long diff;
    for (int i = 1; i < n; i++) {
      diff = live[i] - live[i - 1];
      if (extra / i < diff) {
        return live[i - 1] + extra / i;
      }

      extra -= diff * i;
    }

    return live[n - 1] + extra / n;
  }
};