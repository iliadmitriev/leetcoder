#include <cstdlib>
#include <vector>
using std::vector;

class Solution {

private:
  double inline getAreaTriangle(const vector<int> &p1, const vector<int> &p2,
                                const vector<int> &p3) {
    return std::abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) +
                    p3[0] * (p1[1] - p2[1])) /
           2.0;
  }

public:
  double largestTriangleArea(vector<vector<int>> &points) {
    double curArea = 0.0, maxArea = 0.0;

    int n = points.size();

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        for (int k = j + 1; k < n; k++) {
          curArea = getAreaTriangle(points[i], points[j], points[k]);
          maxArea = std::max(maxArea, curArea);
        }
      }
    }

    return maxArea;
  }
};