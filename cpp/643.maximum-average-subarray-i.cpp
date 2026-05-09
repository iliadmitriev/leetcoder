class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int win = 0, res = 0, i = 0;

        for (; i < k; i++) {
            win += nums[i];
        }

        res = win;

        for (; i < nums.size(); i++) {
            win += nums[i];
            win -= nums[i - k];

            res = max(res, win);
        }

        return double(res) / k;
    }
};