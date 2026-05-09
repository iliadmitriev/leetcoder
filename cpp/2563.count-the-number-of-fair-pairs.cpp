#include <algorithm>
#include <vector>
using std::vector;

class Solution {
private:
  long numberOfPairsLower(const vector<int> &arr, int bound) {
    int left = 0, right = arr.size() - 1;
    int sum;
    long count = 0;

    while (left < right) {
      sum = arr[left] + arr[right];
      if (sum < bound) {
        count += right - left;
        left++;
      } else {
        right--;
      }
    }

    return count;
  }

public:
  long long countFairPairs(vector<int> &nums, int lower, int upper) {
    std::sort(nums.begin(), nums.end());

    long hi = numberOfPairsLower(nums, upper + 1);
    long lo = numberOfPairsLower(nums, lower);

    return hi - lo;
  }
};