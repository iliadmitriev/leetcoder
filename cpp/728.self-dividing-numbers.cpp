#include <vector>
using std::vector;

class Solution {
private:
  bool isSelfDividing(int x) {
    int y = x;

    while (y) {
      int d = y % 10;
      y /= 10;

      if (d == 0 || x % d != 0) {
        return false;
      }
    }

    return true;
  }

public:
  vector<int> selfDividingNumbers(int left, int right) {
    vector<int> nums;

    for (int x = left; x <= right; x++) {
      if (isSelfDividing(x)) {
        nums.push_back(x);
      }
    }

    return nums;
  }
};