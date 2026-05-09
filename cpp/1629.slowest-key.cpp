#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
  char slowestKey(vector<int> &releaseTimes, string keysPressed) {
    int prev = 0;
    char maxDurationKey = 0;
    int maxDuration = 0;

    for (int i = 0; i < releaseTimes.size(); i++) {
      int duration = releaseTimes[i] - prev;
      prev = releaseTimes[i];

      if (duration > maxDuration ||
          (duration == maxDuration && keysPressed[i] > maxDurationKey)) {
        maxDuration = duration;
        maxDurationKey = keysPressed[i];
      }
    }

    return maxDurationKey;
  }
};