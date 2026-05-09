class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int n = nums.size();
        int left = 0; int right = 1;
        int res = right - left;
        long budget = k;

        while (right < n) {
            // be greedy
            // if the rest of the budget is enough to increase all the previous values
            // to the rightmost value then move right pointer of window spending budget
            // how much budget is needed calculated as new rightmost value delta 
            // with previous multiplied by the size of the window
            while (right < n && (long)(nums[right] - nums[right - 1]) * (right - left) <= budget) {
                budget -= (long)(nums[right] - nums[right - 1]) * (right - left);
                right++;
            }

            res = max(res, right - left);

            budget += nums[right - 1] - nums[left];
            left++;
        }

        return res;
    }
};