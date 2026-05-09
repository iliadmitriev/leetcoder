class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int j = 0;
        for (int i = 0; i < nums.size(); i++) {
            std::swap(nums[i], nums[j]);

            if (nums[j] != 0) {
                j++;
            }
        }

        for (int i = j; i < nums.size(); i++) {
            nums[i] = 0;
        }
    }
};