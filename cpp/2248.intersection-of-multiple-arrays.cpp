#include <algorithm>
#include <vector>

using std::vector;

class Solution {
private:
  vector<int> intersect(vector<int> &nums1, vector<int> &nums2) {
    int i = 0, j = 0, k = 0;
    int n1 = nums1.size(), n2 = nums2.size();

    while (i < n1 && j < n2) {
      if (nums1[i] < nums2[j]) {
        i++;
      } else if (nums1[i] > nums2[j]) {
        j++;
      } else {
        nums1[k++] = nums1[i++];
        j++;
      }
    }

    nums1.resize(k);
    return nums1;
  }

public:
  vector<int> intersection(vector<vector<int>> &nums) {
    std::sort(nums[0].begin(), nums[0].end());

    for (int i = 1; i < nums.size(); i++) {
      std::sort(nums[i].begin(), nums[i].end());
      nums[0] = intersect(nums[0], nums[i]);

      if (nums[0].empty()) {
        break;
      }
    }

    return nums[0];
  }
};