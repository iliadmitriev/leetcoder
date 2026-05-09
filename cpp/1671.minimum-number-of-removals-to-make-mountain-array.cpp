#include <vector>
using std::vector;

class Solution {
public:
  int minimumMountainRemovals(vector<int> &nums) {
    int n = nums.size();

    // longest increasing and decreasing subsequences
    vector<int> lis(n, 1), lds(n, 1);

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < i; j++) {
        if (nums[i] > nums[j]) {
          lis[i] = std::max(lis[i], lis[j] + 1);
        }
      }
    }

    for (int i = n - 1; i >= 0; i--) {
      for (int j = i + 1; j < n; j++) {
        if (nums[i] > nums[j]) {
          lds[i] = std::max(lds[i], lds[j] + 1);
        }
      }
    }

    int minRemovals = n;

    for (int i = 1; i < n - 1; i++) {
      if (lis[i] < 2 || lds[i] < 2) {
        continue;
      }

      minRemovals = std::min(minRemovals, n - lis[i] - lds[i] + 1);
    }

    return minRemovals;
  }
};