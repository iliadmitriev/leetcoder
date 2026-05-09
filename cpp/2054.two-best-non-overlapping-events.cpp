#include <algorithm>
#include <vector>
using std::vector;

class Solution {
public:
  int maxTwoEvents(vector<vector<int>> &events) {
    std::sort(events.begin(), events.end());
    const int n = events.size();
    vector<int> suffixMax(n + 1, 0);

    for (int i = n - 1; i >= 0; i--) {
      suffixMax[i] = std::max(suffixMax[i + 1], events[i][2]);
    }

    int maxTwo = 0;

    for (const auto &event : events) {
      int idx = nextMaxIdx(events, event[1] + 1);
      maxTwo = std::max(maxTwo, suffixMax[idx] + event[2]);
    }

    return maxTwo;
  }

private:
  int nextMaxIdx(vector<vector<int>> &arr, int x) {
    int lo = 0, hi = arr.size();
    int mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;
      if (arr[mid][0] < x) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }

    return lo;
  }
};