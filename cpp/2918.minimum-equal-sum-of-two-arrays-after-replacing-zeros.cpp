#include <algorithm>
#include <numeric>
#include <vector>
using std::vector;

class Solution {
public:
  long long minSum(vector<int> &nums1, vector<int> &nums2) {
    const long sumA = std::accumulate(nums1.begin(), nums1.end(), 0LL);
    const long sumB = std::accumulate(nums2.begin(), nums2.end(), 0LL);
    const int zeroA = std::count(nums1.begin(), nums1.end(), 0);
    const int zeroB = std::count(nums2.begin(), nums2.end(), 0);

    if (zeroA == 0 && sumB + zeroB > sumA) {
      return -1;
    }

    if (zeroB == 0 && sumA + zeroA > sumB) {
      return -1;
    }

    return std::max(sumA + zeroA, sumB + zeroB);
  }
};