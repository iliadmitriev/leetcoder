#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
  int countDays(int days, vector<vector<int>> &meetings) {

    std::sort(meetings.begin(), meetings.end(),
              [](const auto &a, const auto &b) -> bool { return a[0] < b[0]; });

    int today = 0;

    for (const auto &meeting : meetings) {
      if (meeting[1] <= today) {
        continue;
      }

      if (today < meeting[0]) {
        days -= meeting[1] - meeting[0] + 1;
      } else {
        days -= meeting[1] - today;
      }

      today = meeting[1];
    }

    return days;
  }
};