#include <algorithm>
#include <vector>

using std::sort;
using std::vector;

class Solution {
private:
  bool isArrangable(vector<int> &position, int m, int d) {
    m--;
    int i = 0;

    for (int j = 1; j < position.size(); j++) {
      if (position[j] - position[i] >= d) {
        m--;
        i = j;
      }

      if (m <= 0) {
        break;
      }
    }

    return m <= 0;
  }

public:
  int maxDistance(vector<int> &position, int m) {
    sort(position.begin(), position.end());
    if (m == 2) {
      return position.back() - position.front();
    }

    int lo = 1, hi = (position.back() - position.front()) / (m - 1);
    while (lo < hi) {
      int mid = (lo + hi + 1) / 2;
      if (isArrangable(position, m, mid)) {
        lo = mid;
      } else {
        hi = mid - 1;
      }
    }

    return lo;
  }
};