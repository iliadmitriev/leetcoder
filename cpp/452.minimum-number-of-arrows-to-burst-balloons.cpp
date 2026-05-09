class Solution {
public:
  int findMinArrowShots(vector<vector<int>> &points) {
    std::sort(points.begin(), points.end(),
              [](const vector<int> &a, const vector<int> &b) -> bool {
                return a[1] < b[1];
              });

    int arrows = 1;
    auto prev_end = points[0][1];

    for (const auto &point : points) {
      if (point[0] > prev_end) {
        arrows++;
        prev_end = point[1];
      }
    }

    return arrows;
  }
};