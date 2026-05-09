class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        int n = nums.size();
        std::sort(nums.begin(), nums.end());
        int op = 0;

        for (int i = n - 1; i > 0; i--) {
            if (nums[i] != nums[i - 1]) {
                op += (n - i);
            }
        }
        return op;
    }
};