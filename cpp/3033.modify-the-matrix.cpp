#include <vector>

using std::vector;

class Solution {
private:
  vector<int> maxCol;
  int getMaxCol(const vector<vector<int>> &matrix, int col) {
    if (maxCol[col] != -1) {
      return maxCol[col];
    }

    for (int i = 0; i < matrix.size(); i++) {
      maxCol[col] = std::max(maxCol[col], matrix[i][col]);
    }

    return maxCol[col];
  }

public:
  vector<vector<int>> modifiedMatrix(vector<vector<int>> &matrix) {
    maxCol = vector<int>(matrix[0].size(), -1);

    for (int i = 0; i < matrix.size(); i++) {
      for (int j = 0; j < matrix[i].size(); j++) {
        if (matrix[i][j] == -1) {
          matrix[i][j] = getMaxCol(matrix, j);
        }
      }
    }

    return matrix;
  }
};