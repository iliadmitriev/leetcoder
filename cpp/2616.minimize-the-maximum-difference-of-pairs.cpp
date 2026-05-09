#include <algorithm>
#include <vector>
using std::vector;

class Solution {
private:
  bool check(const vector<int> &nums, int threshould, int p) {
    const int n = nums.size() - 1;
    int cnt = 0;

    for (int i = 0; i < n; i++) {
      if (nums[i + 1] - nums[i] <= threshould) {
        cnt++;
        i++;
      }

      if (cnt == p) {
        return true;
      }
    }

    return false;
  }

public:
  int minimizeMax(vector<int> &nums, int p) {
    // optimization 1: trivial case
    if (p == 0) {
      return 0;
    }

    std::sort(nums.begin(), nums.end());

    // optimization 2: all pairs should be used (no need to find minimum)
    if (2 * p == nums.size()) {

      int imax = nums[1] - nums[0];
      for (int i = 2; i < nums.size(); i += 2) {
        imax = std::max(imax, nums[i + 1] - nums[i]);
      }
      return imax;
    }

    int lo = 0, hi = nums.back() - nums.front();

    while (lo < hi) {
      int mid = (lo + hi) / 2;

      if (check(nums, mid, p)) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }
};