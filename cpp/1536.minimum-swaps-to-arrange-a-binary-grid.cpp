#include <vector>

using std::vector;

class Solution {
private:
  int leftZeroes(vector<int> &row) {
    for (int i = row.size() - 1; i >= 0; i--) {
      if (row[i] == 1) {
        return row.size() - i - 1;
      }
    }

    return row.size() - 1;
  }

public:
  int minSwaps(vector<vector<int>> &grid) {
    int n = grid.size();
    vector<int> rows(n);
    for (int i = 0; i < n; i++) {
      rows[i] = leftZeroes(grid[i]);
    }

    int swaps = 0;
    int j = 0;

    for (int i = 0; i < n; i++) {
      j = i;

      while (j < n && rows[j] < n - i - 1) {
        j++;
      }

      if (j == n) {
        return -1;
      }

      swaps += j - i;

      while (j > 0) {
        rows[j] = rows[j - 1];
        j--;
      }
    }

    return swaps;
  }
};