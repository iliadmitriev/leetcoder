#include <vector>

using std::vector;

class Solution {
public:
  int chalkReplacer(vector<int> &chalk, int k) {
    int n = chalk.size();

    // optimized
    int total = 0;
    for (int i = 0; i < n; i++) {
      if (total > k) {
        break;
      }

      total += chalk[i];
    }

    k %= total;

    for (int i = 0; i < n; i++) {
      if (k < chalk[i]) {
        return i;
      }

      k -= chalk[i];
    }

    return 0;
  }
};