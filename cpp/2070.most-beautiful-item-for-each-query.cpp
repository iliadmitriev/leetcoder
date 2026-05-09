#include <algorithm>
#include <utility>
#include <vector>

using std::vector, std::pair, std::max, std::sort;

class Solution {
private:
  int binSearch(const vector<pair<int, int>> &data, int target) {
    int lo = 0, hi = data.size();
    int mid;
    while (lo < hi) {
      mid = (lo + hi) / 2;
      if (data[mid].first > target) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }

public:
  vector<int> maximumBeauty(vector<vector<int>> &items, vector<int> &queries) {
    int n = items.size(), m = queries.size();
    vector<int> result(m);

    sort(items.begin(), items.end(),
         [](auto &a, auto &b) { return a[0] < b[0]; });

    vector<pair<int, int>> data({{0, 0}});
    for (int i = 0; i < n; i++) {
      if (data.back().first == items[i][0]) {
        data.back().second = max(data.back().second, items[i][1]);
      } else {
        data.push_back({items[i][0], max(data.back().second, items[i][1])});
      }
    }

    for (int j = 0; j < m; j++) {
      int ix = binSearch(data, queries[j]);
      if (ix > 0) {
        ix--;
      }

      result[j] = data[ix].second;
    }

    return result;
  }
};