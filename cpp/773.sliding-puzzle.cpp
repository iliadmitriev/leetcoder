#include <deque>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

using std::vector, std::string, std::unordered_set, std::deque;

class Solution {
public:
  int slidingPuzzle(vector<vector<int>> &board) {
    vector<vector<int>> moves = {
        {1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4},
    };

    string b;
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j < 3; j++) {
        b.push_back('0' + board[i][j]);
      }
    }

    const string finish = "123450";
    int start = b.find('0');
    unordered_set<string> seen = {b};
    deque<std::pair<int, string>> q = {{start, b}};
    int step = 0;

    while (q.size()) {
      for (int sz = q.size(); sz; sz--) {
        auto [pos, state] = q.front();
        q.pop_front();

        if (state == finish) {
          return step;
        }

        for (int move : moves[pos]) {
          string next(state);
          std::swap(next[pos], next[move]);

          if (seen.count(next)) {
            continue;
          }

          q.push_back({move, next});
          seen.insert(next);
        }
      }

      step++;
    }

    return -1;
  }
};