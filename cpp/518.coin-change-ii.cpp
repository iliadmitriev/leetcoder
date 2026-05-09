class Solution {
private:
    int solve(int amount, int index, vector< vector<int> > &dp, vector<int>& coins) {
        if (amount < 0 || index >= coins.size())
            return 0;

        if (dp[amount][index] != -1)
            return dp[amount][index];

        if (amount == 0)
            return 1;

        return dp[amount][index] = solve(amount - coins[index], index, dp, coins) + solve(amount, index + 1, dp, coins);
    }
public:
    int change(int amount, vector<int>& coins) {
        // init cache
        int n = coins.size();
        vector<vector<int>> dp(amount + 1, vector<int>(n, -1));

        return solve(amount, 0, dp, coins);
    }
};