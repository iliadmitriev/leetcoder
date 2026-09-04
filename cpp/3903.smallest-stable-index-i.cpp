#include <vector>
using std::vector;

class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        const int n = nums.size();
        vector<int> vmax(n, nums.front());
        for (int i = 1; i < n; i++) {
            vmax[i] = std::max(vmax[i - 1], nums[i]);
        }

        vector<int> vmin(n, nums.back());
        for (int i = n - 2; i >= 0; i--) {
            vmin[i] = std::min(vmin[i + 1], nums[i]);
        }

        for (int i = 0; i < n; i++) {
            if (vmax[i] - vmin[i] <= k) {
                return i;
            }
        }

        return -1;
    }
};