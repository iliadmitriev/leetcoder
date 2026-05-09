#include <vector>
using std::vector;

class Solution {
public:
  int maxDistinctElements(vector<int> &nums, int k) {
    // optimize: if k covers all possible lenght of an array twice
    // then in a worst case when all elements are equal, all of them can be
    // unified with such large k
    if (2 * k + 1 > nums.size()) {
      return nums.size();
    }

    std::sort(nums.begin(), nums.end());

    int count = 0;
    int prev = nums.front() - k - 1; // lowest posible value of element

    for (int nums : nums) {
      if (prev < nums - k) {
        prev = nums - k;
        count++;
      } else if (prev < nums + k) {
        prev++;
        count++;
      }
    }

    return count;
  }
};