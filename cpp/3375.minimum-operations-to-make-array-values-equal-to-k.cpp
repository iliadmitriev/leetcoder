#include <vector>
using std::vector;

class Solution {
public:
  int minOperations(vector<int> &nums, int k) {
    vector<int> cnt(101, 0);
    int unique = 0;

    for (int num : nums) {
      if (num < k) {
        return -1;
      }

      if (++cnt[num] == 1) {
        unique++;
      }
    }

    if (cnt[k] == 0) {
      return unique;
    }

    return unique - 1;
  }
};