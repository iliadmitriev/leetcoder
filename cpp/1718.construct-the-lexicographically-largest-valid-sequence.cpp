#include <vector>

using std::vector;

class Solution {
private:
  bool backtrack(vector<int> &seq, vector<bool> used, int idx, int n) {
    if (idx == seq.size()) {
      return true;
    }

    if (seq[idx] != 0) {
      return backtrack(seq, used, idx + 1, n);
    }

    for (int num = n; num >= 1; num--) {
      if (used[num]) {
        continue;
      }

      if (num == 1) {
        used[num] = true;
        seq[idx] = num;

        if (backtrack(seq, used, idx + 1, n)) {
          return true;
        }

        seq[idx] = 0;
        used[num] = false;

      } else {
        if (idx + num >= seq.size() || seq[idx + num] != 0) {
          continue;
        }

        used[num] = true;
        seq[idx] = num;
        seq[idx + num] = num;

        if (backtrack(seq, used, idx + 1, n)) {
          return true;
        }

        used[num] = false;
        seq[idx] = 0;
        seq[idx + num] = 0;
      }
    }

    return false;
  }

public:
  vector<int> constructDistancedSequence(int n) {
    int m = 2 * n - 1;
    vector<bool> used(n + 1, false);
    vector<int> seq(m);

    backtrack(seq, used, 0, n);
    return seq;
  }
};
