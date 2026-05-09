#include <vector>
using std::vector;

class Solution {
private:
  int inline dist(int x, int y, int x0, int y0) {
    return abs(x - x0) + abs(y - y0);
  }

public:
  int nearestValidPoint(int x, int y, vector<vector<int>> &points) {
    int i = -1, dist_min = INT_MAX;

    for (int j = 0; j < points.size(); j++) {
      if (points[j][0] == x || points[j][1] == y) {
        int d = dist(x, y, points[j][0], points[j][1]);
        if (d < dist_min) {
          dist_min = d;
          i = j;
        }
      }
    }

    return i;
  }
};