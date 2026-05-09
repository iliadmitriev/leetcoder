#include <queue>
#include <string>
#include <utility>

using std::string, std::queue;

class Solution {
public:
  string pushDominoes(string dominoes) {
    const int n = dominoes.size();
    queue<std::pair<int, int>> q;

    for (int i = 0; i < n; i++) {
      if (dominoes[i] == 'L' || dominoes[i] == 'R') {
        q.push({i, dominoes[i]});
      }
    }

    while (q.size()) {
      auto [i, d] = q.front();
      q.pop();

      if (d == 'L') {
        if (i > 0 && dominoes[i - 1] == '.') {
          dominoes[i - 1] = 'L';
          q.push({i - 1, 'L'});
        }
      } else if (i + 1 < n && dominoes[i + 1] == '.') {
        if (i + 2 < n && dominoes[i + 2] == 'L') {
          q.pop();
        } else {
          dominoes[i + 1] = 'R';
          q.push({i + 1, 'R'});
        }
      }
    }

    return dominoes;
  }
};