#include <vector>
#include <functional>
#include <numeric>

using std::vector;

constexpr int MOD = int(1e9) + 7;

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
      int m = r - l + 1;

      vector<int> dp0(m, 1), dp1(m, 1); // base case 1 combination
      vector<int> sum0(m + 1, 0), sum1(m + 1, 0);

      for (int i = 1; i < n; i++) {
        for (int j = 0; j < m; j++) {
          sum0[j + 1] = (sum0[j] + dp0[j]) % MOD;
          sum1[j + 1] = (sum1[j] + dp1[j]) % MOD;
        }

        for (int j = 0; j < m; j++) {
          dp0[j] = (sum1[m] - sum1[j + 1] + MOD) % MOD;
          dp1[j] = sum0[j];
        }
      }

      std::function<int(int,int)> op = [](int acc, int x) -> int {
        return (acc + x) % MOD;
      };

      int ans0 = std::reduce(dp0.begin(), dp0.end(), 0, op);
      int ans1 = std::reduce(dp1.begin(), dp1.end(), 0, op);

      return (ans0 + ans1) % MOD;
    }
};