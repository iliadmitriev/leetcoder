class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        vector<int> res(nums.size(), -1);

        if (nums.size() <= 2 * k) {
            return res;
        }

        long window = 0;
        for (int i = 0; i < 2 * k; i++) {
            window += nums[i];
        }

        for (int i = k; i < nums.size() - k; i++) {
            window += nums[i + k];
            res[i] = window / (2 * k + 1);
            window -= nums[i - k];
        }
        return res;
    }
};