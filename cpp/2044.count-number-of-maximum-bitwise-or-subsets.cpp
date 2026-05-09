#include <numeric>
#include <vector>
using std::vector, std::accumulate;

class Solution {
private:
  int bitCount(int i, int cur, const vector<int> &nums, int target) {
    if (i == nums.size()) {
      return cur == target ? 1 : 0;
    }

    return bitCount(i + 1, cur, nums, target) +
           bitCount(i + 1, cur | nums[i], nums, target);
  }

public:
  int countMaxOrSubsets(vector<int> &nums) {
    int target = accumulate(nums.begin(), nums.end(), 0,
                            [](int a, int b) { return a | b; });

    return bitCount(0, 0, nums, target);
  }
};