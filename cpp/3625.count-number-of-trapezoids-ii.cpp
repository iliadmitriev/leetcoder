#include <limits>
#include <unordered_map>
#include <vector>

using std::unordered_map, std::vector, std::pair;

class Solution {
public:
  int countTrapezoids(vector<vector<int>> &points) {
    const int INF = std::numeric_limits<float>::infinity();
    const int n = points.size();

    unordered_map<float, vector<float>> slopes;
    unordered_map<int, vector<float>> mids;

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        int x1 = points[i][0], y1 = points[i][1];
        int x2 = points[j][0], y2 = points[j][1];

        int dx = x1 - x2;
        int dy = y1 - y2;

        float k, b;

        if (x1 == x2) {
          k = INF;
          b = float(x1);
        } else {
          k = float(y2 - y1) / float(x2 - x1);
          b = (float(y1) * dx - float(x1) * dy) / dx;
        }

        slopes[k].push_back(b);
        mids[(x1 + x2) * 10000 + y1 + y2].push_back(k);
      }
    }

    int ans = 0;

    // count number of total parallel pairs
    for (auto &[_, b] : slopes) {
      if (b.size() < 2) {
        continue;
      }

      unordered_map<float, int> cnt;
      for (auto x : b) {
        cnt[x]++;
      }

      int total = 0;
      for (auto [_, c] : cnt) {
        ans += total * c;
        total += c;
      }
    }

    // minus parallelograms and collinear
    for (auto &[_, k] : mids) {
      if (k.size() < 2) {
        continue;
      }

      unordered_map<float, int> cnt;
      for (auto x : k) {
        cnt[x]++;
      }

      int total = 0;
      for (auto [_, c] : cnt) {
        ans -= total * c;
        total += c;
      }
    }

    return ans;
  }
};