#include <numeric>
#include <vector>
using std::vector;

class Solution {
private:
  bool checkDistribution(int n, const vector<int> &quantities, long maxBucket) {
    for (int q : quantities) {
      n -= q / maxBucket + (q % maxBucket > 0);
      if (n < 0) {
        return false;
      }
    }

    return true;
  }

public:
  int minimizedMaximum(int n, vector<int> &quantities) {
    int maxBucket = quantities.front();
    long total = std::accumulate(quantities.begin(), quantities.end(), 0LL);

    long lo = std::max(1L, total / n), hi = total;
    long mid;
    while (lo < hi) {
      mid = (lo + hi) / 2;
      if (checkDistribution(n, quantities, mid)) {
        hi = mid;
        maxBucket = mid;
      } else {
        lo = mid + 1;
      }
    }

    return maxBucket;
  }
};