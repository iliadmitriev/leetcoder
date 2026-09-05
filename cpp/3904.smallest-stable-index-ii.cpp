#include <vector>
#include <utility>

using std::vector;

class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        const int n = nums.size();
        
        int vmax = nums.front();
        vector<int> vmin(n, nums.back());

        for (int i = n - 2; i >= 0; i--) {
          vmin[i] = std::min(vmin[i + 1], nums[i]);
        }

        for (int i = 0; i < n; i++) {
          vmax = std::max(vmax, nums[i]);

          if (vmax - vmin[i] <= k) {
            return i;
          }
        }

        return -1;
    }
};