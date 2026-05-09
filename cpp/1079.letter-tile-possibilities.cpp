#include <array>
#include <string>

using std::string, std::array;

class Solution {
private:
  typedef array<int, 26> alpha;
  int backtrack(string &tiles, int idx, alpha &used) {
    int total = 0;

    for (int i = 0; i < 26; i++) {
      if (!used[i]) {
        continue;
      }

      total++;

      used[i]--;
      total += backtrack(tiles, idx + 1, used);
      used[i]++;
    }

    return total;
  }

public:
  int numTilePossibilities(string tiles) {
    alpha voc;

    for (char c : tiles) {
      voc[c - 'A']++;
    }

    return backtrack(tiles, 0, voc);
  }
};