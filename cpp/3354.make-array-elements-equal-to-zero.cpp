#include <numeric>
#include <vector>
using std::vector;

class Solution {
public:
  int countValidSelections(vector<int> &nums) {
    int selections = 0;

    int left = 0, right = std::accumulate(nums.begin(), nums.end(), 0);

    for (int num : nums) {
      left += num;
      right -= num;

      if (num != 0) {
        continue;
      }

      int diff = std::abs(left - right);

      if (diff == 0) {
        selections += 2;
      } else if (diff == 1) {
        selections += 1;
      }
    }

    return selections;
  }
};