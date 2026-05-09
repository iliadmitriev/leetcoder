#include <algorithm>
#include <utility>
#include <vector>

using std::vector, std::pair;

class Solution {
private:
  bool checkValid(vector<pair<int, int>> &intervals) {
    int count = 0, right = 0;

    std::sort(intervals.begin(), intervals.end());

    for (auto [l, r] : intervals) {
      if (l >= right) {
        count++;
      }

      right = std::max(right, r);
      if (count >= 3) {
        return true;
      }
    }

    return count >= 3;
  }

public:
  bool checkValidCuts(int n, vector<vector<int>> &rectangles) {
    const int m = rectangles.size();
    vector<pair<int, int>> X, Y;
    X.reserve(m), Y.reserve(m);

    for (const auto &rect : rectangles) {
      X.emplace_back(rect[0], rect[2]);
      Y.emplace_back(rect[1], rect[3]);
    }

    return checkValid(X) || checkValid(Y);
  }
};