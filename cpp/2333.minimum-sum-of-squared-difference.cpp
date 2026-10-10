#include <vector>
using std::vector;

class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1,
                               int k2) {
        long long total = 0, ops = long(k1) + long(k2);
        const int n = nums1.size();
        int mx = 0;

        for (int i = 0; i < n; i++) {
            mx = std::max(mx, std::abs(nums1[i] - nums2[i]));
        }

        vector<int> diff_count(mx + 1, 0);

        for (int i = 0; i < n; i++) {
            diff_count[std::abs(nums1[i] - nums2[i])]++;
        }

        int op;

        for (int v = mx; v > 0 && ops > 0; v--) {
            if (ops >= diff_count[v]) {
                op = diff_count[v];
            } else {
                op = ops;
            }

            ops -= op;
            diff_count[v] -= op;
            diff_count[v - 1] += op;
        }

        long long res = 0;
        for (int v = mx; v > 0; v--) {
            res += 1LL * v * v * diff_count[v];
        }

        return res;
    }
};