#include <vector>
using std::vector;

class Solution {
public:
  int numberOfPairs(vector<vector<int>> &points) {
    const int n = points.size();
    int count = 0;

    // sort x ascending, y descending
    std::sort(points.begin(), points.end(),
              [](const vector<int> &a, const vector<int> &b) -> bool {
                return a[0] < b[0] || (a[0] == b[0] && a[1] > b[1]);
              });

    int maxY, minY, negInf = std::numeric_limits<int>::min();

    for (int i = 0; i < n; i++) {
      maxY = points[i][1];
      minY = negInf;

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