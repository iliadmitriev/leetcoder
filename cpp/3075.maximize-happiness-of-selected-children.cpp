#include <algorithm>
#include <functional>
#include <vector>

using std::vector;

class Solution {
public:
  long long maximumHappinessSum(vector<int> &happiness, int k) {
    typedef long long ll;

    ll total = 0;

    std::sort(happiness.begin(), happiness.end(), std::greater<>());

    for (int j = 0; j < k; j++) {
      int value = std::max(0, happiness[j] - j);

      if (value == 0) {
        break;
      }

      total += value;
    }

    return total;
  }
};