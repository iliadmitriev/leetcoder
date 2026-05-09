#include <vector>

using std::vector;

class Solution {
public:
  int oddCells(int m, int n, vector<vector<int>> &indices) {
    vector<int> rows(m, 0), cols(n, 0);

    for (int i = 0; i < indices.size(); ++i) {
      rows[indices[i][0]] ^= 1;
      cols[indices[i][1]] ^= 1;
    }

    int rowOdd = 0, rowEven = 0, colOdd = 0, colEven = 0;

    for (int r : rows) {
      rowOdd += r;
      rowEven += (1 - r);
    }

    for (int c : cols) {
      colOdd += c;
      colEven += (1 - c);
    }

    return rowOdd * colEven + rowEven * colOdd;
  }
};