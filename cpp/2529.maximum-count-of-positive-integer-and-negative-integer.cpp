#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
  int maximumCount(vector<int> &nums) {
    const int n = nums.size();

    if (nums.back() < 0) {
      return n;
    }

    if (nums.front() > 0) {
      return n;
    }

    int zeroIns = binSearchLeft(nums, 0);
    int oneIns = binSearchRight(nums, 0);

    return std::max(zeroIns, n - oneIns);
  }

private:
  int binSearchLeft(const vector<int> &arr, int target) {
    int lo = 0, hi = arr.size();
    int mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (arr[mid] < target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }

    return lo;
  }

  int binSearchRight(const vector<int> &arr, int target) {
    int lo = 0, hi = arr.size();
    int mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (arr[mid] <= target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo;
  }
};