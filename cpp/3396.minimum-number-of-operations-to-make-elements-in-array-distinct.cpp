#include <vector>
using std::vector;

class Solution {
public:
  int minimumOperations(vector<int> &nums) {
    vector<int> cnt(101, 0);

    for (int i = nums.size() - 1; i >= 0; i--) {
      if (++cnt[nums[i]] == 2) {
        return i / 3 + 1;
      }
    }

    return 0;
  }
};