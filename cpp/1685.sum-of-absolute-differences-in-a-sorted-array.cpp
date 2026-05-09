class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 0);

        int prefix = 0;
        int suffix = accumulate(nums.begin(), nums.end(), 0);

        for (int i = 0; i < n; i++) {
            res[i] = i * nums[i] - prefix + suffix - (n - i) * nums[i];
            prefix += nums[i];
            suffix -= nums[i];
        }

        return res;   
    }
};