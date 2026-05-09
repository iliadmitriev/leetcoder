#include <vector>

using std::vector;

class Solution {
private:
  int popCount(int n) {
    int count = 0;

    while (n) {
      n &= n - 1;
      count++;
    }

    return count;
  }

public:
  int sumIndicesWithKSetBits(vector<int> &nums, int k) {
    int total = 0;

    for (int i = 0; i < nums.size(); i++) {
      if (k == popCount(i)) {
        total += nums[i];
      }
    }

    return total;
  }
};