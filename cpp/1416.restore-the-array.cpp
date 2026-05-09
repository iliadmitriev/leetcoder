class Solution {
public:
    int numberOfArrays(string s, int k) {
        int MOD = 1e9 + 7;
        int n = s.size();
        vector<int> dp(n + 1, 0);
        dp[n] = 1;

        for (int i = n - 1; i >= 0; i--) {

            if (s[i] == '0') {
                continue;
            }


            size_t len = 1; // start length from 0 to maximum
            long count = 0;
            long num = s[i] - '0';
            while (num <= k && i + len <= s.size()) {
                count += dp[i + len];
                num *= 10;
                num += s[i + len] - '0';
                len++;
            }

            dp[i] = count % MOD;
        }

        return dp[0];
    }
};