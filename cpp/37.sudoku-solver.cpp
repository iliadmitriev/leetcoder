#include <utility>
#include <vector>
using std::vector, std::pair;

class Solution {
private:
  const int N = 9;
  const int ALL = (1 << (N + 1)) - 1;
  const char EMPTY = '.';
  const char BASE = '1';

  bool dfs(vector<vector<char>> &board, vector<int> &rows, vector<int> &cols,
           vector<int> &boxes, vector<pair<int, int>> &empties, int i) {
    if (i == empties.size()) {
      return true;
    }

    auto [r, c] = empties[i];
    int available = rows[r] & cols[c] & boxes[r / 3 * 3 + c / 3];

    if (!available) {
      return false;
    }

    for (int j = 0; j < N; j++) {
      int can = 1 << j;
      if (!(available & can)) {
        continue;
      }

      rows[r] ^= can;
      cols[c] ^= can;
      boxes[r / 3 * 3 + c / 3] ^= can;

      board[r][c] = BASE + j;

      if (dfs(board, rows, cols, boxes, empties, i + 1)) {
        return true;
      }

      rows[r] ^= can;
      cols[c] ^= can;
      boxes[r / 3 * 3 + c / 3] ^= can;
    }
    return false;
  }

public:
  void solveSudoku(vector<vector<char>> &board) {

    vector<int> rows(N, ALL), cols(N, ALL), boxes(N, ALL);
    vector<pair<int, int>> empties;

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (board[i][j] == EMPTY) {
          empties.push_back({i, j});
        } else {
          int mask = 1 << (board[i][j] - BASE);
          rows[i] ^= mask;
          cols[j] ^= mask;
          boxes[i / 3 * 3 + j / 3] ^= mask;
        }
      }
    }

    dfs(board, rows, cols, boxes, empties, 0);
  }
};