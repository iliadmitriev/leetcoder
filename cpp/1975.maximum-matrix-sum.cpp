#include <iostream>
#include <vector>
using std::vector;

const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  long long maxMatrixSum(vector<vector<int>> &matrix) {
    long long total = 0;
    int n = matrix.size();
    int minAbs = std::abs(matrix.front().front());
    int countNeg = 0;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        int value = matrix[i][j];

        countNeg += value < 0;

        value = value < 0 ? -value : value;

        if (value < minAbs) {
          minAbs = value;
        }

        total += value;
      }
    }

    if (countNeg % 2 == 0) {
      return total;
    }

    return total - 2 * minAbs;
  }
};