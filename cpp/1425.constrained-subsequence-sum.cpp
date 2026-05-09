class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        std::deque<int> q; // monotonic double ended queue, greatest value at front
        std::vector<int> dp(nums.size(), 0);
        int out = nums[0];

        for (int i = 0; i < nums.size(); i++) {
            // drop from the start of queue
            // all values with indexes greater than window size
            while (!q.empty() && i - q.front() > k) {
                q.pop_front();
            }

            // calculate current value
            dp[i] = nums[i];
            if (!q.empty()) {
                dp[i] += dp[q.front()];
            }

            // drop from the end of queue
            // all values less or equal to current value
            while (!q.empty() && dp[q.back()] <= dp[i]) {
                q.pop_back();
            }

            if (dp[i] > 0) {
                q.push_back(i);
            }

            // find max
            out = max(out, dp[i]);

        }
        return out;
    }
};