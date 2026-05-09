#include <vector>

using std::max;
using std::min;
using std::vector;

class Solution {
private:
  bool isValid(vector<int> &bloomDay, int mid, int m, int k) {
    int j = 0;
    for (auto bd : bloomDay) {
      if (bd <= mid) {
        ++j;
      } else {
        j = 0;
      }
      if (j == k) {
        --m;
        j = 0;
      }
      if (m == 0) {
        break;
      }
    }
    return m == 0;
  }

public:
  int minDays(vector<int> &bloomDay, int m, int k) {
    if (bloomDay.size() < long(m) * k) {
      return -1;
    }
    int lo = bloomDay.front(), hi = bloomDay.back(), mid;
    for (auto bd : bloomDay) {
      lo = min(lo, bd);
      hi = max(hi, bd);
    }

    while (lo < hi) {
      mid = (lo + hi) / 2;
      if (isValid(bloomDay, mid, m, k)) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }
};