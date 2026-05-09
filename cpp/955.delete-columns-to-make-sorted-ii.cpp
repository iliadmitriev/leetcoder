#include <string>
#include <vector>
using std::vector, std::string;

class Solution {
public:
  int minDeletionSize(vector<string> &strs) {
    int rows = strs.size(), cols = strs.front().size();
    int removed = 0;

    vector<bool> inOrder(rows, false);

    for (int c = 0; c < cols; c++) {
      bool broken = false;

      for (int r = 1; r < rows; r++) {
        if (inOrder[r]) {
          continue;
        }

        if (strs[r - 1][c] > strs[r][c]) {
          broken = true;
          break;
        }
      }

      if (broken) {
        removed++;
        continue;
      }

      for (int r = 1; r < rows; r++) {
        if (!inOrder[r] && strs[r - 1][c] < strs[r][c]) {
          inOrder[r] = true;
        }
      }
    }

    return removed;
  }
};