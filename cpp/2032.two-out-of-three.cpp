#include <vector>

using std::vector;

class Solution {
public:
  vector<int> twoOutOfThree(vector<int> &nums1, vector<int> &nums2,
                            vector<int> &nums3) {

    const int n = 101;

    vector<int> set1(n, 0), set2(n, 0), set3(n, 0);

    for (int num : nums1)
      set1[num] = 1;
    for (int num : nums2)
      set2[num] = 1;
    for (int num : nums3)
      set3[num] = 1;

    vector<int> res;
    for (int i = 0; i < n; i++) {
      if (set1[i] + set2[i] + set3[i] > 1)
        res.push_back(i);
    }

    return res;
  }
};