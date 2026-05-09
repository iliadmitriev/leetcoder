class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        int target = total - x;

        // optimize 1
        if (target < 0) {
            return -1;
        }
        // optimize 2
        if (target == 0) {
            return nums.size();
        }

        int curr_total = 0;
        int left = 0;
        int n = int(nums.size());
        int res = std::numeric_limits<int>::max();

        for (int right = 0; right < n; right++) {
            // increase count and current total from right pointer
            curr_total += nums[right];

            // decrease count and current total from left pointer
            // if curr_total is exceeding the target
            while (left <= right && curr_total > target) {
                curr_total -= nums[left];
                left++;
            }
            // if we able to collect target
            // check if it's less than minimal
            if (curr_total == target) {
                res = min(res, n - (right - left + 1));
            }
        }

        return res != std::numeric_limits<int>::max() ? res : -1;
    }
};