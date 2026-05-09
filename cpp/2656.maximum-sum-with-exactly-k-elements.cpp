#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
  int maximizeSum(vector<int> &nums, int k) {
    int first = *std::max_element(nums.begin(), nums.end());
    int last = first + k - 1;

    return k * (first + last) / 2;
  }
};