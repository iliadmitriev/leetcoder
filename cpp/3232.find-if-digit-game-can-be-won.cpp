#include <vector>

using std::vector;

class Solution {
public:
  bool canAliceWin(vector<int> &nums) {
    int sngl = 0, dbl = 0;

    for (int num : nums) {
      if (num < 10) {
        sngl += num;
      } else {
        dbl += num;
      }
    }

    return sngl < dbl || sngl > dbl;
  }
};