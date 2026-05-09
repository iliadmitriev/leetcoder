#include <vector>

using std::max;
using std::vector;

class Solution {
public:
  int maxSatisfied(vector<int> &customers, vector<int> &grumpy, int minutes) {
    int satisfiedNotGrumpy = 0;
    int satisfiedGrumpyWindow = 0;
    int maxSatisfiedGrumpy = 0;

    for (int i = 0; i < customers.size(); ++i) {
      // count satisfied customers when not grumpy
      satisfiedNotGrumpy += customers[i] * (1 - grumpy[i]);

      // count satisfied customers when grumpy with window size of minutes
      satisfiedGrumpyWindow += customers[i] * grumpy[i];
      if (i >= minutes)
        satisfiedGrumpyWindow -= customers[i - minutes] * grumpy[i - minutes];
      // count max satisfied customers when grumpy
      maxSatisfiedGrumpy = max(maxSatisfiedGrumpy, satisfiedGrumpyWindow);
    }

    return satisfiedNotGrumpy + maxSatisfiedGrumpy;
  }
};