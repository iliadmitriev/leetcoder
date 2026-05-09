#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
  vector<vector<int>> mergeArrays(vector<vector<int>> &nums1,
                                  vector<vector<int>> &nums2) {
    vector<vector<int>> res;
    res.reserve(std::min(nums1.size(), nums2.size()));

    int i = 0, j = 0;

    while (i < nums1.size() && j < nums2.size()) {
      if (nums1[i][0] < nums2[j][0]) {
        res.push_back(nums1[i++]);
      } else if (nums1[i][0] > nums2[j][0]) {
        res.push_back(nums2[j++]);
      } else {
        res.push_back({nums1[i][0], nums1[i++][1] + nums2[j++][1]});
      }
    }

    res.insert(res.end(), nums1.begin() + i, nums1.end());
    res.insert(res.end(), nums2.begin() + j, nums2.end());

    return res;
  }
};