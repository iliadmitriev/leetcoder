#include <cstdlib>
#include <numeric>
#include <vector>
using std::vector;

class Solution {
public:
  int largestSumAfterKNegations(vector<int> &nums, int k) {
    // sort descending order by an absolute value
    std::sort(nums.begin(), nums.end(),
              [&](int a, int b) { return abs(a) > abs(b); });

    // use k to make biggest negative values positive
    for (int i = 0; i < nums.size() && k > 0; ++i) {
      if (nums[i] < 0) {
        nums[i] = -nums[i];
        --k;
      }
    }

    // if it's still k left, just make
    // smallest absolute value negative
    if (k % 2) {
      nums.back() = -nums.back();
    }

    // return total sum
    return std::accumulate(nums.begin(), nums.end(), 0);
  }
};