#include <vector>
using std::vector;

const int N = 9, D = 3;
const char EMPTY = '.', BASE = '1';

class Solution {
private:
  // check if field of 9 cells is valid
  // field can be one of 9x1, 3x3 or 1x9
  // field is set by it's top left corner (row y, col x) and size (width)
  bool checkField(int y, int x, int size, const vector<vector<char>> &board) {
    vector<int> tmp(N + 1, 0);

    for (int i = 0; i < N; i++) {
      char ch = board[y + i / size][x + i % size];

      if (ch == EMPTY) {
        continue;
      }

      if (++tmp[ch - BASE] > 1) {
        return false;
      }
    }
    return true;
  }

public:
  bool isValidSudoku(vector<vector<char>> &board) {

    for (int i = 0; i < N; i++) {
      if (!checkField(0, i, 1, board)) {
        return false;
      }

      if (!checkField(i, 0, N, board)) {
        return false;
      }

      if (!checkField(i / D * D, i % D * D, D, board)) {
        return false;
      }
    }

    return true;
  }
};