#include <algorithm>
#include <vector>

using std::sort;
using std::vector;

class Solution {
public:
  int getMaximumConsecutive(vector<int> &coins) {
    int cover = 0;
    sort(coins.begin(), coins.end());

    for (int i = 0; i < coins.size() && cover + 1 >= coins[i]; ++i) {
      cover += coins[i];
    }

    return cover + 1;
  }
};