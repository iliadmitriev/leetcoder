#include <vector>
using std::vector;

class Solution {
public:
  long long countSubarrays(vector<int> &nums, int minK, int maxK) {
    const int n = nums.size();
    int left = -1, right = -1, cut = -1;
    long total = 0;

    for (int i = 0; i < n; i++) {
      if (nums[i] < minK || nums[i] > maxK) {
        left = right = -1;
        cut = i;
      }

      if (nums[i] == minK) {
        left = i;
      }

      if (nums[i] == maxK) {
        right = i;
      }

      if (left != -1 && right != -1) {
        total += std::min(left, right) - cut;
      }
    }

    return total;
  }
};