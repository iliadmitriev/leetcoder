#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
public:
  long long maximumTotalDamage(vector<int> &power) {
    unordered_map<int, int> cnt;

    long long dp = 0, dp1 = 0, dp2 = 0,
              dp3 = 0;  // three previous max gained damage
    int p1 = 0, p2 = 0; // pointers for two previous used powers

    for (int pwr : power) {
      cnt[pwr]++;
    }

    vector<int> powers;
    powers.reserve(cnt.size());
    for (auto [k, v] : cnt) {
      powers.push_back(k);
    }

    std::sort(powers.begin(), powers.end());

    for (int pwr : powers) {
      long long value = 1LL * pwr * cnt[pwr];

      dp = std::max(dp3 + value, std::max(dp2, dp1));

      if (pwr - p2 > 2) {
        dp = std::max(dp, dp2 + value);
      }

      if (pwr - p1 > 2) {
        dp = std::max(dp, dp1 + value);
      }

      dp3 = dp2;
      dp2 = dp1;
      dp1 = dp;

      p2 = p1;
      p1 = pwr;
    }

    return dp;
  }
};