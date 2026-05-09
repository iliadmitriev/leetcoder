class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();

        // xor - both repeated and missing number
        int xor_ = 0; 
        for (int i = 1; i <= n; i++) {
            xor_ ^= i ^ nums[i - 1];
        }

        // get different bit for repeated and missing numbers
        int rightmost = xor_ & ~(xor_ - 1);

        // separate repeated and missing number with different bit
        int xor0 = 0, xor1 = 0;
        for (int i = 1; i <= n; i++) {
            if (nums[i - 1] & rightmost) {
                xor0 ^= nums[i - 1];
            } else {
                xor1 ^= nums[i - 1];
            }

            if (i & rightmost) {
                xor0 ^= i;
            } else {
                xor1 ^= i;
            }
        }

        // if xor0 present in original set it's repeated number and xor1 is missing
        for (int num: nums) {
            if (xor0 == num) {
                return {xor0, xor1};
            }
        }

        // otherwise
        return {xor1, xor0};
    }
};