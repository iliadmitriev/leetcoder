
#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
  vector<vector<int>> restoreMatrix(vector<int> &rowSum, vector<int> &colSum) {
    int m = rowSum.size(), n = colSum.size();
    vector<vector<int>> mat(m, vector<int>(n));

    int i = 0, j = 0;
    while (i < m && j < n) {
      mat[i][j] = std::min(rowSum[i], colSum[j]);
      if (rowSum[i] == colSum[j]) {
        i++;
        j++;
      } else if (rowSum[i] > colSum[j]) {
        rowSum[i] -= colSum[j];
        j++;
      } else {
        colSum[j] -= rowSum[i];
        i++;
      }
    }

    return mat;
  }
};