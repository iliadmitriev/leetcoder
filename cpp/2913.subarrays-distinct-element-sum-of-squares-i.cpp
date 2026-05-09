#include <unordered_set>
#include <vector>

using std::unordered_set;
using std::vector;

class Solution {
public:
  int sumCounts(vector<int> &nums) {
    int res = 0, n = nums.size();

    for (int i = 0; i < n; i++) {
      unordered_set<int> seen;

      for (int j = i; j < n; j++) {
        seen.insert(nums[j]);
        res += seen.size() * seen.size();
      }
    }

    return res;
  }
};