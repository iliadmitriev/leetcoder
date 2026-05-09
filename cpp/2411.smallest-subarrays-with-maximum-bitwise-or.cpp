#include <vector>
using std::vector;

class Solution {
public:
  vector<int> smallestSubarrays(vector<int> &nums) {
    const int n = nums.size();
    vector<int> ans(n, 1);

    for (int i = 0; i < n; i++) {
      int x = nums[i];
      int j = i - 1;

      while (j >= 0 && (x | nums[j]) != nums[j]) {
        nums[j] |= x;
        ans[j] = i - j + 1;
        j--;
      }
    }

    return ans;
  }
};