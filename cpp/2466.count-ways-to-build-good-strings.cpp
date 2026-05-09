class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        const int bottom = high + 2;
        long dp[bottom]; memset(dp, 0, sizeof(dp));
        long mod = int(1e9 + 7);

        for (int i = high; i >= 0; i--) {
            dp[i] = (int(i >= low) + dp[min(high + 1, i + one)] + dp[min(high + 1, i + zero)]) % mod;
        }

        return dp[0];
    }
};