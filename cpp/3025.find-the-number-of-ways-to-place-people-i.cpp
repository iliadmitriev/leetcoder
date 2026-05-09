#include <vector>
using std::vector;

class Solution {
public:
  int numberOfPairs(vector<vector<int>> &points) {
    int count = 0;
    const int n = points.size();
    const int inf = std::numeric_limits<int>::min();

    std::sort(points.begin(), points.end(),
              [](const vector<int> &a, const vector<int> &b) -> bool {
                // a[0] ascending
                // a[1] descending
                return a[0] < b[0] || (a[0] == b[0] && a[1] > b[1]);
              });

    for (int i = 0; i < n; i++) {
      int maxY = points[i][1];
      int minY = inf;

      for (int j = i + 1; j < n; j++) {
        if (minY < points[j][1] && points[j][1] <= maxY) {
          count++;
          minY = points[j][1];
        }

        if (maxY == minY) {
          break;
        }
      }
    }

    return count;
  }
};