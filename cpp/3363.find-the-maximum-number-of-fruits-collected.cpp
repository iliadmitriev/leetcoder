#include <vector>
using std::vector;

class Solution {
public:
  int maxCollectedFruits(vector<vector<int>> &fruits) {
    const int n = fruits.size();
    int total = 0;

    for (int i = 0; i < n; i++) {
      total += fruits[i][i];
    }

    vector<int> cur = vector<int>(n, 0), pre = vector<int>(n, 0);
    pre[n - 1] = fruits[0][n - 1];

    // left part between digonals
    for (int i = 1; i < n - 1; i++) {
      for (int j = std::max(i + 1, n - 1 - i); j < n; j++) {
        cur[j] = pre[j];

        if (j - 1 >= 0) {
          cur[j] = std::max(cur[j], pre[j - 1]);
        }

        if (j + 1 < n) {
          cur[j] = std::max(cur[j], pre[j + 1]);
        }

        cur[j] += fruits[i][j];
      }

      pre.swap(cur);
    }

    vector<int> cur2 = vector<int>(n, 0), pre2 = vector<int>(n, 0);
    pre2[n - 1] = fruits[n - 1][0];

    // bottom part between diagonals
    for (int i = 1; i < n - 1; i++) {
      for (int j = std::max(i + 1, n - 1 - i); j < n; j++) {
        cur2[j] = pre2[j];

        if (j - 1 >= 0) {
          cur2[j] = std::max(cur2[j], pre2[j - 1]);
        }

        if (j + 1 < n) {
          cur2[j] = std::max(cur2[j], pre2[j + 1]);
        }

        cur2[j] += fruits[j][i];
      }

      pre2.swap(cur2);
    }

    total += pre[n - 1];
    total += pre2[n - 1];

    return total;
  }
};