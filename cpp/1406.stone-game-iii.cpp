class Solution {
public:
    string stoneGameIII(vector<int>& stoneValue) {
        int n = stoneValue.size();

        // accumulated stoneValues (prefix sum starting with 0)
        vector<int> value(n + 1, 0);
        partial_sum(stoneValue.begin(), stoneValue.end(), value.begin() + 1);

        // bottom up dp
        vector<int> dp(n + 1, 0);
        for (int pos = n; pos >= 0; pos--) {
            // calculate max for each step size
            dp[pos] = max({
                value[min(n, pos + 1)] - value[pos] - dp[min(n, pos + 1)],
                value[min(n, pos + 2)] - value[pos] - dp[min(n, pos + 2)],
                value[min(n, pos + 3)] - value[pos] - dp[min(n, pos + 3)]
            });
        }

        if (dp[0] > 0) {
            return "Alice";
        } else if (dp[0] < 0) {
            return "Bob";
        }
        return "Tie";
    }
};