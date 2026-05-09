#include <vector>

using std::vector;

class Solution {
public:
  vector<int> findIntersectionValues(vector<int> &nums1, vector<int> &nums2) {
    vector<int> cache1(101, 0);
    vector<int> cache2(101, 0);

    for (int num : nums1) {
      cache1[num] = 1;
    }

    for (int num : nums2) {
      cache2[num] = 1;
    }

    int res1 = 0, res2 = 0;
    for (int num : nums1) {
      res1 += cache2[num];
    }

    for (int num : nums2) {
      res2 += cache1[num];
    }

    return {res1, res2};
  }
};