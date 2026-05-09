#include <vector>
using std::vector;

class Solution {
public:
  long long maximumTripletValue(vector<int> &nums) {
    long res = 0;
    int prefix = 0, diff = 0;

    for (int num : nums) {
      res = std::max(res, long(diff) * num);
      prefix = std::max(prefix, num);
      diff = std::max(diff, prefix - num);
    }

    return res;
  }
};