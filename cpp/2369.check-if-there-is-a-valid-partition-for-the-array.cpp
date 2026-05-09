class Solution {
public:
    bool validPartition(vector<int>& nums) {
        int n = nums.size();

        bool A = true, B = false, C = nums[0] == nums[1];
        bool temp_B, temp_C;

        for (int i = 2; i < n; i++) {
            temp_B = B; temp_C = C;

            C = (B && nums[i - 1] == nums[i]) // 2 numbers are equal
                || A && (
                    (nums[i - 2] == nums[i - 1] && nums[i - 1] == nums[i]) // 3 numbers are equal
                    || (nums[i - 2] + 1 == nums[i - 1] && nums[i - 1] + 1 == nums[i]) // 3 numbers are increasing by 1
                );
            B = temp_C;
            A = temp_B;

            // optimization
            if (!(A || B || C))
                break;
        };

        return C;
    }
};