#include <vector>
using std::vector;

class Solution {
public:
  vector<int> findDiagonalOrder(vector<vector<int>> &mat) {
    const int m = mat.size(), n = mat.front().size();
    const int size = m * n;
    vector<int> diag;
    diag.reserve(size);
    // observations:
    // 1. if sum of both indexes is even, moving up right (and it's remains even
    // until hit the right or top boundary)
    // 2. if sum of both indexes is odd, moving down left (and it's remains
    // odd until hit the bottom or left boundary)
    int i = 0, j = 0;

    for (int k = size; k > 0; k--) {
      diag.push_back(mat[i][j]);

      if (((i + j) & 1) == 0) { // if moving up-right
        if (j == n - 1) {       // and hit the right boundary
          i++;                  // move down to the next row
        } else if (i == 0) {    // or hit the top boundary
          j++;                  // move right to the next column
        } else {
          i--; // move up
          j++; // move right
        }
      } else {               // if moving down left
        if (i == m - 1) {    // and hit the bottom boundary
          j++;               // move right to then next column
        } else if (j == 0) { // or hit the left boundary
          i++;               // move down to the next row
        } else {
          i++; // move down
          j--; // move left
        }
      }
    }

    return diag;
  }
};