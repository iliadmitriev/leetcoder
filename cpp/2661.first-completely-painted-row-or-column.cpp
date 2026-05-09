#include <vector>

using std::vector;

class Solution {
public:
  int firstCompleteIndex(vector<int> &arr, vector<vector<int>> &mat) {

    const int nrows = mat.size();
    const int ncols = mat.back().size();
    const int ncels = nrows * ncols;

    vector<int> rows(nrows, ncols), cols(ncols, nrows);
    vector<int> rowsIdx(ncels + 1, 0), colsIdx(ncels + 1, 0);

    for (int i = 0; i < nrows; ++i) {
      for (int j = 0; j < ncols; ++j) {
        rowsIdx[mat[i][j]] = i;
        colsIdx[mat[i][j]] = j;
      }
    }

    for (int idx = 0; idx < arr.size(); ++idx) {
      int row = --rows[rowsIdx[arr[idx]]];
      int col = --cols[colsIdx[arr[idx]]];

      if (row == 0 || col == 0) {
        return idx;
      }
    }

    return -1;
  }
};