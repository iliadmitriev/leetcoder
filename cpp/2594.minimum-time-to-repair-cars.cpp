#include <algorithm>
#include <cmath>
#include <vector>
using std::vector;

class Solution {
public:
  long long repairCars(vector<int> &ranks, int cars) {
    const int m = ranks.size();
    long long maxRank = *std::max_element(ranks.begin(), ranks.end());
    long long lo = 0, hi = std::pow(cars / m + 1LL, 2) * maxRank;
    long long mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (isTimeEnough(ranks, mid, cars)) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }

private:
  bool isTimeEnough(const vector<int> &ranks, long long time, int cars) {
    for (int rank : ranks) {
      cars -= int(std::sqrt(time / rank));
      if (cars <= 0) {
        return true;
      }
    }
    return false;
  }
};