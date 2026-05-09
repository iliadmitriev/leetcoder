#include <vector>

using std::vector;

class Solution {
public:
  vector<vector<int>> matrixReshape(vector<vector<int>> &mat, int r, int c) {
    int R = mat.size(), C = mat[0].size();

    if (R == r && C == c) {
      return mat;
    }

    if (R * C != r * c) {
      return mat;
    }

    vector<vector<int>> res(r, vector<int>(c));

    for (int i = 0; i < r * c; i++) {
      res[i / c][i % c] = mat[i / C][i % C];
    }

    return res;
  }
};