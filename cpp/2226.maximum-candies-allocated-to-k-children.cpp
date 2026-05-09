#include <numeric>
#include <vector>

using std::vector;

class Solution {
private:
  bool check(const vector<int> &candies, long long k, int v) {
    for (int i = 0; i < candies.size(); ++i) {
      k -= candies[i] / v;
      if (k <= 0) {
        return true;
      }
    }

    return false;
  }

public:
  int maximumCandies(vector<int> &candies, long long k) {
    long long sum = std::accumulate(candies.begin(), candies.end(), 0LL);

    if (k > sum) {
      return 0;
    }

    int res = 0;
    int lo = 1, hi = (sum / k) + 1, mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (check(candies, k, mid)) {
        res = mid;
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }

    return res;
  }
};