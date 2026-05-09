class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int left = 0, right = 0;
        int n = nums.size();

        for (int i = 1; i < n; i++) { right += nums[i]; }

        if (left == right) {
            return 0;
        }

        for (int i = 1; i < n; i++) {
            left += nums[i - 1];
            right -= nums[i];
            if (left == right) {
                return i;
            }
        }

        return -1;
    }
};