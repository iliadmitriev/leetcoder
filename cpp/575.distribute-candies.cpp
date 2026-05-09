#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
  int distributeCandies(vector<int> &candyType) {
    std::sort(candyType.begin(), candyType.end());

    int unique = 1;
    for (int i = 1; i < candyType.size(); i++) {
      if (candyType[i] != candyType[i - 1]) {
        unique++;
      }
    }

    return std::min(unique, int(candyType.size()) / 2);
  }
};