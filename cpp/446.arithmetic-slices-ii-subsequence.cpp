class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int n = nums.size();
        vector<unordered_map<long, int>> dp(n, unordered_map<long, int>());

        int res = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                long diff = long(nums[i]) - nums[j];
                dp[i][diff] += dp[j][diff] + 1;
                res += dp[j][diff];
            }
        }

        return res;
    }
};