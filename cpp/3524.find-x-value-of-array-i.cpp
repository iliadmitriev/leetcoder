/*
 0 1 2 3 4
[1,2,3,4,5], k = 3

the number itselt mod k
the product and number mod k

1  [0,1,0]

 */
#include <vector>
using std::vector;

class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        if (k == 1) {
            long long n = nums.size();
            return {n * (n + 1) / 2};
        }

        vector<long long> res(k, 0LL);
        // two state dp array:
        // i & 1 - current
        // i & 1 ^ 1 - previous
        vector<vector<long long>> dp(2, vector<long long>(k, 0LL));
        const int n = nums.size();

        for (int i = 0; i < n; i++) {
            // reset current vector
            std::ranges::fill(dp[i & 1], 0LL);
            // add the number mod k itself
            dp[i & 1][nums[i] % k]++;

            for (int r = 0; r < k; r++) {
                // if previous step remainder subarrays count > 0
                if (dp[i & 1 ^ 1][r] > 0) {
                    dp[i & 1][1LL * nums[i] * r % k] += dp[i & 1 ^ 1][r];
                }
            }

            for (int r = 0; r < k; r++) {
                res[r] += dp[i & 1][r];
            }
        }

        return res;
    }
};