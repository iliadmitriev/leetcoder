
#include <algorithm>
#include <vector>

using std::vector;

class Solution {
private:
  bool __bisectLeft(const vector<int> &arr, int target, int diff) {
    int mid;
    int lo = 0, hi = arr.size();

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (arr[mid] < target) {
        if (target - arr[mid] <= diff) {
          return false;
        }

        lo = mid + 1;
      } else {
        if (arr[mid] - target <= diff) {
          return false;
        }

        hi = mid;
      }
    }

    return true;
  }

public:
  int findTheDistanceValue(vector<int> &arr1, vector<int> &arr2, int d) {
    int res = 0;

    std::sort(arr2.begin(), arr2.end());

    for (int x : arr1) {
      if (__bisectLeft(arr2, x, d)) {
        res++;
      }
    }

    return res;
  }
};