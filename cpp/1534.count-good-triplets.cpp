#include <vector>

using std::vector;

class Solution {
private:
  // find rightmost x position in the arr
  int bisectRight(const vector<int> &arr, int x) {
    int lo = 0, hi = arr.size();
    int mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (x < arr[mid]) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }

  // leftmost position of x in the arr
  int bisectLeft(const vector<int> &arr, int x) {
    int lo = 0, hi = arr.size();
    int mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (arr[mid] < x) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }

    return lo;
  }
  // insert x to the rightmost position
  void insortRight(vector<int> &arr, int x) {
    int idx = bisectRight(arr, x);
    arr.insert(arr.begin() + idx, x);
  }

public:
  int countGoodTriplets(vector<int> &arr, int a, int b, int c) {
    int count = 0, n = arr.size();

    for (int j = n - 2; j >= 0; j--) {

      vector<int> arr_b;
      for (int k = j + 1; k < n; k++) {
        int diff = arr[j] - arr[k];

        if (abs(diff) <= b) {
          insortRight(arr_b, diff);
        }
      }

      for (int i = 0; i < j; i++) {
        int diff = arr[i] - arr[j];
        if (abs(diff) <= a) {
          int lower = bisectLeft(arr_b, -c - diff);
          int upper = bisectRight(arr_b, c - diff);
          count += upper - lower;
        }
      }
    }

    return count;
  }
};