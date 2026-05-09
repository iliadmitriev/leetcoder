#include <vector>

using std::vector;

class Solution {
private:
  long long max(long long a, long long b) {
    if (a > b) {
      return a;
    }
    return b;
  }

public:
  long long maxPoints(vector<vector<int>> &points) {
    int m = points.size(), n = points[0].size();

    vector<long long> row(points[0].begin(), points[0].end());

    for (int i = 1; i < m; i++) {
      vector<long long> left(n, 0);
      left[0] = row[0];
      for (int j = 1; j < n; j++) {
        left[j] = max(row[j], left[j - 1] - 1);
      }

      vector<long long> right(n, 0);
      right[n - 1] = row[n - 1];
      for (int j = n - 2; j >= 0; j--) {
        right[j] = max(row[j], right[j + 1] - 1);
      }

      for (int j = 0; j < n; j++) {
        row[j] = max(left[j], right[j]) + points[i][j];
      }
    }

    return *std::max_element(row.begin(), row.end());
  }
};