#include <numeric>
#include <vector>
using std::vector;

class Solution {
public:
  int xorAllNums(vector<int> &nums1, vector<int> &nums2) {
    int len1 = nums1.size(), len2 = nums2.size();
    int xor1 = std::accumulate(nums1.begin(), nums1.end(), 0,
                               [](int res, int x) { return res ^ x; });
    int xor2 = std::accumulate(nums2.begin(), nums2.end(), 0,
                               [](int res, int x) { return res ^ x; });

    int ans = 0;

    if (len1 % 2) {
      ans ^= xor2;
    }

    if (len2 % 2) {
      ans ^= xor1;
    }

    return ans;
  }
};