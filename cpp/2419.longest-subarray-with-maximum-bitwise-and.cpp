#include <vector>
using std::vector;

class Solution {
public:
  int longestSubarray(vector<int> &nums) {
    int count = 0, maxCount = 0;
    int maxEl = -1;

    for (int n : nums) {

      if (n == maxEl) {
        count++;
        if (count > maxCount) {
          maxCount = count;
        }
      } else if (n > maxEl) {
        maxEl = n;
        count = 1;
        maxCount = 1;
      } else {
        count = 0;
      }
    }

    return maxCount;
  }
};