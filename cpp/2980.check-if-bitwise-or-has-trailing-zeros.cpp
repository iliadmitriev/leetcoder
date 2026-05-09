#include <vector>
using std::vector;

class Solution {
public:
  bool hasTrailingZeros(vector<int> &nums) {
    int cnt = 0;

    for (int num : nums) {
      cnt += !(num & 1);

      if (cnt > 1)
        return true;
    }

    return false;
  }
};