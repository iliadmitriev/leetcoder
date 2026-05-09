#include <vector>
using std::vector;

typedef vector<vector<int>> Matrix;

class Solution {

public:
  int countSquares(Matrix &matrix) {
    int m = matrix.size(), n = matrix.back().size();
    Matrix dp(m + 1, vector<int>(n + 1, 0));

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (matrix[i][j] == 1) {
          dp[i + 1][j + 1] =
              std::min({dp[i][j + 1], dp[i + 1][j], dp[i][j]}) + 1;
        }
      }
    }

    int count = 0;
    for (int i = 0; i <= m; i++) {
      for (int j = 0; j <= n; j++) {
        count += dp[i][j];
      }
    }
    return count;
  }
};