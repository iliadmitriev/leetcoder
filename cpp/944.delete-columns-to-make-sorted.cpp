#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
  int minDeletionSize(vector<string> &strs) {
    int rows = strs.size(), cols = strs.front().size();
    int removed = 0;

    for (int c = 0; c < cols; c++) {
      for (int r = 1; r < rows; r++) {
        if (strs[r - 1][c] > strs[r][c]) {
          removed++;
          break;
        }
      }
    }

    return removed;
  }
};