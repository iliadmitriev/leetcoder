#include <vector>

using std::vector;

class Solution {
public:
  int findPoisonedDuration(vector<int> &timeSeries, int duration) {
    int poisoned = 0, prev = -1;

    for (int tm : timeSeries) {
      if ((prev == -1) || (prev + duration <= tm)) {
        poisoned += duration;
      } else {
        poisoned += tm - prev;
      }

      prev = tm;
    }

    return poisoned;
  }
};