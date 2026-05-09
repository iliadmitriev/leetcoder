#include <vector>
using std::vector;

class Solution {
public:
  int maxFreeTime(int eventTime, vector<int> &startTime, vector<int> &endTime) {
    const int n = startTime.size();
    vector<int> spaces(n + 1);
    int prev = 0;

    for (int i = 0; i < n; i++) {
      spaces[i] = startTime[i] - prev;
      prev = endTime[i];
    }

    spaces[n] = eventTime - prev;

    // get indexes of the 3 biggest empty spaces
    // in worst case 2 of them can be occupied
    // and last one can be perfect candiate for movement
    int first = -1, second = -1, third = -1;
    for (int i = 0; i <= n; i++) {
      if (first == -1 || spaces[i] > spaces[first]) {
        third = second;
        second = first;
        first = i;
      } else if (second == -1 || spaces[i] > spaces[second]) {
        third = second;
        second = i;
      } else if (third == -1 || spaces[i] > spaces[third]) {
        third = i;
      }
    }

    int maxFree = 0;

    for (int i = 0; i < n; i++) {
      int len = endTime[i] - startTime[i];
      int left = spaces[i], right = spaces[i + 1];

      maxFree = std::max(maxFree, left + right);

      // if there is an vacant empty space not occupied by left(i) or right(i +
      // 1) meeting and this space is longer then current meeting lenght try to
      // move meeting to this space
      if ((i != first && i + 1 != first && len <= spaces[first]) ||
          (i != second && i + 1 != second && len <= spaces[second]) ||
          (i != third && i + 1 != third && len <= spaces[third])) {
        maxFree = std::max(maxFree, left + len + right);
      }
    }

    return maxFree;
  }
};