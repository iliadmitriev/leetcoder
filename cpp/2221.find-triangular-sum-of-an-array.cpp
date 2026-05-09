class Solution {
public:
    int triangularSum(vector<int>& nums) {
        for (int i = nums.size(); i >= 0; i--) {
            for (int j = 1; j < i; j++) {
                nums[j - 1] = (nums[j - 1] + nums[j]) % 10;
            }
        }
        return nums[0];
    }
};