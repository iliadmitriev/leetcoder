#include <algorithm>
#include <vector>
using std::vector;

class Solution {
private:
  int countPairs(vector<int> &nums, int diff) {
    int count = 0, left = 0;
    for (int right = 1; right < nums.size(); right++) {
      while (nums[right] - nums[left] > diff) {
        left++;
      }

      count += right - left;
    }

    return count;
  }

public:
  int smallestDistancePair(vector<int> &nums, int k) {
    std::sort(nums.begin(), nums.end());

    int lo = 0, hi = nums.back() - nums.front() + 1;
    int mid;

    while (lo < hi) {
      mid = (hi + lo) / 2;

      if (countPairs(nums, mid) >= k) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }
};