#include <vector>
using std::vector;

class Solution {
private:
  int zeroPos(vector<int> &arr, int lo, int hi) {
    // int mid;
    //
    // while (lo < hi) {
    //   mid = (lo + hi) / 2;
    //   if (arr[mid] >= 0) {
    //     lo = mid + 1;
    //   } else {
    //     hi = mid;
    //   }
    // }
    //
    // return lo;

    for (int i = hi; i > lo; i--) {
      if (arr[i - 1] >= 0) {
        return i;
      }
    }

    return 0;
  }

public:
  int countNegatives(vector<vector<int>> &grid) {
    const int m = grid.size(), n = grid.front().size();

    int count = 0, cur = n;

    for (int i = 0; i < m; i++) {
      cur = zeroPos(grid[i], 0, cur);

      count += n - cur;
    }

    return count;
  }
};