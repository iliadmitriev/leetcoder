#include <numeric>
#include <unordered_set>
#include <vector>

using std::vector, std::unordered_set;

class Solution {
public:
  int maxSum(vector<int> &nums) {
    unordered_set<int> seen;
    int ma = nums[0];
    bool pos = false;

    for (int num : nums) {
      if (num >= 0) {
        seen.insert(num);
        pos = true;
      } else {

        ma = std::max(ma, num);
      }
    }

    if (!pos) {
      return ma;
    }

    return std::accumulate(seen.begin(), seen.end(), 0);
  }
};