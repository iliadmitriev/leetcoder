#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
  string tictactoe(vector<vector<int>> &moves) {
    // 3 rows, 3 cols, 2 diagonals (total 8)
    vector<int> A(8, 0), B(8, 0);

    for (int i = 0; i < moves.size(); i++) {
      // set pointer on player A or B depending on the turn parity
      auto &p = i % 2 == 0 ? A : B;

      int r = moves[i][0], c = moves[i][1];
      p[r]++;
      p[3 + c]++;
      p[6] += int(r == c);
      p[7] += int(r == 2 - c);
    }

    for (int j = 0; j < 8; j++) {
      if (A[j] == 3)
        return "A";
      if (B[j] == 3)
        return "B";
    }

    return moves.size() == 9 ? "Draw" : "Pending";
  }
};