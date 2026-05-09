#include <vector>

using std::vector;

class Solution {
public:
  int arithmeticTriplets(vector<int> &nums, int diff) {
    int count = 0;
    int n = nums.size();
    vector<bool> dbl(200, false), tpl(200, false);

    for (int num : nums) {
      if (tpl[num]) {
        count++;
      }

      if (dbl[num]) {
        tpl[num + diff] = true;
      }

      dbl[num + diff] = true;
    }

    return count;
  }
};