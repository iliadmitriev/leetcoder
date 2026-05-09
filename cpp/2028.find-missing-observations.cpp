#include <numeric>
#include <vector>
using std::vector;

class Solution {
public:
  vector<int> missingRolls(vector<int> &rolls, int mean, int n) {
    int m = rolls.size();
    int total = (m + n) * mean;

    total -= std::accumulate(rolls.begin(), rolls.end(), 0);

    if (total < n || total > n * 6) {
      return {};
    }

    vector<int> res(n);

    for (int i = 0; i < n; ++i) {
      res[i] = total / n;
    }

    for (int i = 0; i < total % n; ++i) {
      res[i] += 1;
    }

    return res;
  }
};