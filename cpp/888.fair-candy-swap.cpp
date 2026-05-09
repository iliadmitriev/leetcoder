#include <numeric>
#include <unordered_set>
#include <vector>

using std::unordered_set;
using std::vector;

class Solution {
public:
  vector<int> fairCandySwap(vector<int> &aliceSizes, vector<int> &bobSizes) {
    int totalAlice = std::accumulate(aliceSizes.begin(), aliceSizes.end(), 0);
    int totalBob = std::accumulate(bobSizes.begin(), bobSizes.end(), 0);

    unordered_set<int> bobSet(bobSizes.begin(), bobSizes.end());
    int draw = (totalAlice + totalBob) / 2;
    int diff = draw - totalAlice;

    for (int alice : aliceSizes) {
      if (bobSet.count(diff + alice)) {
        return {alice, diff + alice};
      }
    }

    return {0, 0};
  }
};