#include <vector>
using std::vector;

class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        const int n = nums.size();
        vector<int> res(n);

        // write pointers
        int l = 0, r = n - 1;

        // read pointers
        for (int i = 0, j = n - 1; i < n; i++, j--) {
            if (nums[i] < pivot) {
                res[l++] = nums[i];
            }

            if (nums[j] > pivot) {
                res[r--] = nums[j];
            }
        }

        // fill the gap
        for (int i = l; i <= r; i++) {
            res[i] = pivot;
        }

        return res;
    }
};