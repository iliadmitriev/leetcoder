#include <array>
#include <vector>
using std::vector, std::array;

class Solution {
public:
  int numEquivDominoPairs(vector<vector<int>> &dominoes) {
    int total = 0;
    array<array<int, 10>, 10> cache;

    for (const auto &domino : dominoes) {
      int a = domino[0], b = domino[1];
      if (a > b) {
        std::swap(a, b);
      }

      total += cache[a][b];
      cache[a][b]++;
    }

    return total;
  }
};