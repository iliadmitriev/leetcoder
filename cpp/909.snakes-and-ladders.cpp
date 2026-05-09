#include <queue>
#include <utility>
#include <vector>
using std::vector, std::queue, std::pair;

class Solution {
public:
  int snakesAndLadders(vector<vector<int>> &board) {
    const int m = board.size(), n = board.front().size();
    const int start = 1, finish = m * n;
    const int size = finish + 1;

    queue<pair<int, int>> q;       // queue of {position, moves}
    vector<bool> vis(size, false); // mark visited positions

    vector<int> b(size, -1); // lined up board
    bool ltr = true;         // left to right

    for (int i = 0, r = m - 1; r >= 0; r--) { // bottom to top
      if (ltr) {
        for (int c = 0; c < n; c++) { // odd right to left
          b[++i] = board[r][c];
        }
      } else {
        for (int c = n - 1; c >= 0; c--) { // even left to right
          b[++i] = board[r][c];
        }
      }
      ltr = !ltr;
    }

    q.push({start, 0});
    vis[start] = true;

    while (q.size()) {
      auto [pos, move] = q.front();
      q.pop();

      if (pos == finish) {
        return move;
      }

      for (int i = 6; i >= 1; i--) { // roll the dice: 6 to 1
        int next = std::min(pos + i, finish);

        // if snake or ladder
        if (b[next] != -1) {
          next = b[next];
        }

        if (!vis[next]) {
          vis[next] = true;
          q.push({next, move + 1});
        }
      }
    }

    return -1;
  }
};