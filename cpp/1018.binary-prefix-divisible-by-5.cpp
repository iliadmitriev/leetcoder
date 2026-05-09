#include <vector>
using std::vector;

class Solution {
public:
  vector<bool> prefixesDivBy5(vector<int> &nums) {
    int cur = 0;
    vector<bool> res;
    res.reserve(nums.size());

    for (int num : nums) {
      cur <<= 1;
      cur += num;
      cur %= 5;

      res.push_back(cur == 0);
    }

    return res;
  }
};