#include <vector>
using std::vector;

class Solution {
public:
  int areaOfMaxDiagonal(vector<vector<int>> &dimensions) {
    int maxArea = 0, maxDiagonal = 0;

    for (const auto &dim : dimensions) {
      int diagonal = dim[0] * dim[0] + dim[1] * dim[1];

      if (diagonal > maxDiagonal) {
        maxDiagonal = diagonal;
        maxArea = dim[0] * dim[1];
      } else if (diagonal == maxDiagonal) {
        maxArea = std::max(maxArea, dim[0] * dim[1]);
      }
    }

    return maxArea;
  }
};