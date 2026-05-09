#include <vector>
using std::vector;

class Solution {
public:
  long long countAlternatingSubarrays(vector<int> &nums) {
    long total = 0L;

    int cur = -1, curLen = 0;

    for (int num : nums) {
      if (num == cur) {
        curLen = 1;
      } else {
        curLen++;
      }

      total += curLen;
      cur = num;
    }

    return total;
  }
};