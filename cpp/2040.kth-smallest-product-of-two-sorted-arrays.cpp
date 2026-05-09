#include <vector>
using std::vector;

class Solution {
private:
  int bisectRight(const vector<int> &arr, int x) {
    int lo = 0, hi = arr.size();
    int mid;

    while (lo < hi) {
      mid = lo + (hi - lo) / 2;

      if (x < arr[mid]) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }

  int bisectLeft(const vector<int> &arr, int x) {
    int lo = 0, hi = arr.size();
    int mid;

    while (lo < hi) {
      mid = lo + (hi - lo) / 2;

      if (arr[mid] < x) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }

    return lo;
  }

  long long count(const vector<int> &nums1, const vector<int> &nums2,
                  long long target) {
    long long total = 0;

    for (int num1 : nums1) {
      if (num1 == 0) {
        if (target >= 0)
          total += nums2.size();
        continue;
      }

      int lo = 0, hi = nums2.size();

      while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        long long prod = long(num1) * nums2[mid];

        if (prod <= target) {
          if (num1 > 0)
            lo = mid + 1;
          else
            hi = mid;
        } else {
          if (num1 > 0)
            hi = mid;
          else
            lo = mid + 1;
        }
      }

      if (num1 > 0)
        total += lo;
      else
        total += nums2.size() - lo;
    }

    return total;
  }

public:
  long long kthSmallestProduct(vector<int> &nums1, vector<int> &nums2,
                               long long k) {
    if (nums1.size() > nums2.size())
      return kthSmallestProduct(nums2, nums1, k);

    long long left = 1LL * nums1[0] * nums2[0];
    long long right = 1LL * nums1[0] * nums2[0];

    for (int i : {0, int(nums1.size()) - 1}) {
      for (int j : {0, int(nums2.size()) - 1}) {
        left = std::min(left, 1LL * nums1[i] * nums2[j]);
        right = std::max(right, 1LL * nums1[i] * nums2[j]);
      }
    }

    while (left < right) {
      long long mid = left + (right - left) / 2;
      long long cnt = count(nums1, nums2, mid);
      if (cnt < k) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    return left;
  }
};