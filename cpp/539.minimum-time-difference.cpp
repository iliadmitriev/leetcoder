#include <algorithm>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  int findMinDifference(vector<string> &timePoints) {
    const int day = 24 * 60;
    int n = timePoints.size();
    vector<int> times;
    times.reserve(n);

    for (const string &time : timePoints) {
      times.push_back(60 * std::stoi(time.substr(0, 2)) +
                      std::stoi(time.substr(3, 2)));
    }

    std::sort(times.begin(), times.end());

    int minDiff = day;

    for (int i = 1; i < n; ++i) {
      minDiff = std::min(minDiff, times[i] - times[i - 1]);
    }

    return std::min(minDiff, (day - times.back() + times.front()) % day);
  }
};