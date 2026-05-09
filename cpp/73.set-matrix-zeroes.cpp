#include <vector>
using std::vector;

class Solution {
public:
  void setZeroes(vector<vector<int>> &matrix) {
    const int m = matrix.size(), n = matrix.front().size();
    vector<bool> row(m, false), col(n, false);

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (matrix[i][j] == 0) {
          row[i] = true;
          col[j] = true;
        }
      }
    }

    for (int i = 0; i < m; i++) {
      if (!row[i]) {
        continue;
      }

      for (int j = 0; j < n; j++) {
        matrix[i][j] = 0;
      }
    }

    for (int j = 0; j < n; j++) {
      if (!col[j]) {
        continue;
      }

      for (int i = 0; i < m; i++) {
        matrix[i][j] = 0;
      }
    }
  }
};