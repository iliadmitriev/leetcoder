#include <utility>
#include <vector>

using std::pair;
using std::vector;

class Solution {
private:
  pair<int, int> findFigure(vector<vector<char>> &board, char figure) {
    for (int i = 0; i < board.size(); ++i) {
      for (int j = 0; j < board[0].size(); ++j) {
        if (board[i][j] == figure) {
          return {i, j};
        }
      }
    }

    return {-1, -1};
  }

public:
  int numRookCaptures(vector<vector<char>> &board) {
    auto [rookRow, rookCol] = findFigure(board, 'R');
    int res = 0;
    const vector<pair<int, int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    for (auto [dr, dc] : dirs) {
      int r = rookRow, c = rookCol;
      while (r >= 0 && r < board.size() && c >= 0 && c < board.back().size() &&
             board[r][c] != 'B') {
        if (board[r][c] == 'p') {
          res++;
          break;
        }
        r += dr;
        c += dc;
      }
    }

    return res;
  }
};