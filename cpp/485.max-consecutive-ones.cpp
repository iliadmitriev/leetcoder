#include <algorithm>
#include <vector>

using std::max;
using std::vector;

class Solution {
public:
  int findMaxConsecutiveOnes(vector<int> &nums) {
    int maxCnt = 0, cnt = 0;
    for (auto num : nums) {
      if (num == 1) {
        cnt++;
        maxCnt = max(maxCnt, cnt);
      } else {
        cnt = 0;
      }
    }

    return maxCnt;
  }
};