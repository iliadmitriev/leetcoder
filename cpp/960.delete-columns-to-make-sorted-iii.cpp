#include <algorithm>
#include <string>
#include <vector>
using std::vector, std::string;

class Solution {
public:
  int minDeletionSize(vector<string> &strs) {
    const int ROWS = strs.size();
    const int COLS = strs.front().size();
    int removed = COLS - 1; // worst case remove all but one
    int k;

    vector<int> dp(COLS, 1);

    for (int i = 1; i < COLS; i++) {
      for (int j = 0; j < i; j++) {

        for (k = 0; k < ROWS; ++k) {
          if (strs[k][j] > strs[k][i]) {
            break;
          }
        }

        if (k == ROWS && dp[j] + 1 > dp[i]) {
          dp[i] = dp[j] + 1;
        }
      }

      removed = std::min(removed, COLS - dp[i]);
    }

    return removed;
  }
};