#include <algorithm>
#include <numeric>
#include <vector>

using std::max;
using std::sort;
using std::vector;

class Solution {
public:
  int maxProfitAssignment(vector<int> &difficulty, vector<int> &profit,
                          vector<int> &worker) {
    int maxProfit = 0, maxEarning = 0;
    int j = 0;
    sort(worker.begin(), worker.end());
    vector<int> indexes(difficulty.size());
    std::iota(indexes.begin(), indexes.end(), 0);

    sort(indexes.begin(), indexes.end(), [&](int i, int j) {
      if (difficulty[i] == difficulty[j]) {
        return profit[i] < profit[j];
      }
      return difficulty[i] < difficulty[j];
    });

    for (auto w : worker) {
      while (j < indexes.size() && w >= difficulty[indexes[j]]) {
        maxEarning = max(maxEarning, profit[indexes[j++]]);
      }
      maxProfit += maxEarning;
    }

    return maxProfit;
  }
};