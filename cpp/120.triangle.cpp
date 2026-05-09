#include <algorithm>
#include <vector>
using std::vector;

class Solution {
public:
  int minimumTotal(vector<vector<int>> &triangle) {
    // for (int i = triangle.size() - 2; i >= 0; i--) {
    //   for (int j = 0; j < triangle[i].size(); j++) {
    //     triangle[i][j] += std::min(triangle[i + 1][j], triangle[i + 1][j +
    //     1]);
    //   }
    // }
    //
    // return triangle[0][0];

    for (int i = 1; i < triangle.size(); i++) {
      for (int j = 0; j < triangle[i].size(); j++) {
        if (j == 0) {
          triangle[i][j] += triangle[i - 1][j];
        } else if (j == i) {
          triangle[i][j] += triangle[i - 1][j - 1];
        } else {
          triangle[i][j] +=
              std::min(triangle[i - 1][j], triangle[i - 1][j - 1]);
        }
      }
    }

    return *std::min_element(triangle.back().begin(), triangle.back().end());
  }
};