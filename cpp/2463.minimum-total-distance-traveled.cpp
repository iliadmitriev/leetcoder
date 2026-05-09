#include <cstdlib>
#include <numeric>
#include <vector>
using std::vector;
class Solution {
public:
  long long minimumTotalDistance(vector<int> &robot,
                                 vector<vector<int>> &factory) {
    // sort robots and factories
    std::sort(robot.begin(), robot.end());
    std::sort(factory.begin(), factory.end());

    int robotCount = robot.size();

    int factoriesCount =
        std::accumulate(factory.begin(), factory.end(), 0,
                        [](int res, auto &f) -> int { return res + f[1]; });

    vector<int> factories;
    factories.reserve(factoriesCount);
    for (const auto &f : factory) {
      for (int i = 0; i < f[1]; i++) {
        factories.push_back(f[0]);
      }
    }

    vector<vector<long long>> dp(robotCount + 1,
                                 vector<long long>(factoriesCount + 1, -1));
    for (int i = 0; i <= factoriesCount; i++) {
      dp[robotCount][i] = 0;
    }

    for (int i = robotCount - 1; i >= 0; i--) {
      for (int j = factoriesCount - 1; j >= 0; j--) {
        if (dp[i + 1][j + 1] >= 0) {
          int diff = std::abs(factories[j] - robot[i]);
          dp[i][j] = dp[i][j] != -1
                         ? std::min(dp[i][j], dp[i + 1][j + 1] + diff)
                         : dp[i + 1][j + 1] + diff;
        }

        if (dp[i][j + 1] >= 0) {
          dp[i][j] =
              dp[i][j] != -1 ? std::min(dp[i][j], dp[i][j + 1]) : dp[i][j + 1];
        }
      }
    }

    return dp[0][0];
  }
};