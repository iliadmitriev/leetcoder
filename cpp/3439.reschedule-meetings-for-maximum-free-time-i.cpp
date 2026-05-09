#include <vector>
using std::vector;

class Solution {
public:
  int maxFreeTime(int eventTime, int k, vector<int> &startTime,
                  vector<int> &endTime) {
    vector<int> spaces;
    const int n = startTime.size();
    spaces.reserve(n + 1);

    int prev = 0;
    for (int i = 0; i < n; i++) {
      spaces.push_back(startTime[i] - prev);
      prev = endTime[i];
    }
    spaces.push_back(eventTime - prev);

    const int m = spaces.size();
    int freeTime = 0, maxFreeTime = 0;

    for (int right = 0; right < m; right++) {
      freeTime += spaces[right];

      if (right - k - 1 >= 0) {
        freeTime -= spaces[right - k - 1];
      }

      maxFreeTime = std::max(maxFreeTime, freeTime);
    }

    return maxFreeTime;
  }
};