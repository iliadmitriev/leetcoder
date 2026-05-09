#include <stdexcept>
#include <vector>

using std::vector;

class Solution {
public:
  int maxDistance(int side, vector<vector<int>> &points, int k) {
    const int n = points.size();

    /*
    counterclockwise unfold:

    bottom: y = 0, d = x;
    right: x = side, d = side + y;
    top: y = side, d = 3 * side - x;
    left: x = 0, d = 4 * side - y;

    last and first correlates: 4 * side - x; // clockwise
    */
    auto toDist = [side](vector<int> &s) -> long {
      int x = s[0], y = s[1];

      if (y == 0) {
        return x;
      } else if (x == side) {
        return 1L * side + y;
      } else if (y == side) {
        return 3L * side - x;
      } else if (x == 0) {
        return 4L * side - y;
      }

      throw std::invalid_argument("point is not on the side of the square");
    };

    vector<long> dist(n, 0);

    // transform and sort
    std::transform(points.begin(), points.end(), dist.begin(), toDist);
    std::sort(dist.begin(), dist.end());

    long lo = 1, hi = 4LL * side / k, mid;
    int res = 0;

    /*
    check if there is a possible way to get k elements from dist array with
    the difference between two adjacent elements at least limit
    from each starting distance element try to find k elements
    */
    auto check = [&dist, side, k](long long limit) -> bool {
      // try each element as start
      for (long long start : dist) {
        // the end of the range to search should not be grater then perimeter
        long long end = start + 4LL * side - limit;
        long long cur = start;

        // try get k - 1 elements (not including start)
        for (int i = 0; i < k - 1; i++) {
          auto it = std::lower_bound(dist.begin(), dist.end(), cur + limit);

          if (it == dist.end() || *it > end) {
            cur = -1;
            break;
          }

          cur = *it; // move to the next
        }

        if (cur >= 0) {
          return true;
        }
      }

      return false;
    };

    while (lo <= hi) {
      mid = (lo + hi) / 2;

      if (check(mid)) {
        lo = mid + 1;
        res = mid;
      } else {
        hi = mid - 1;
      }
    }

    return res;
  }
};