#include <vector>
using std::vector;

class Solution {
public:
  int maxScoreSightseeingPair(vector<int> &values) {
    int maxScore = -values[0];
    int curScore = 0;
    int n = values.size();

    for (int i = 0; i < n; i++) {
      maxScore = std::max(maxScore, curScore + values[i] - i);
      curScore = std::max(curScore, values[i] + i);
    }

    return maxScore;
  }
};