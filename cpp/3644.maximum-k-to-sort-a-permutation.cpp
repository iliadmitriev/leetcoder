class Solution {
public:
    int sortPermutation(vector<int>& nums) {
        const int n = nums.size();
        int res = -1;

        for (int i = 0; i < n; i++) {
            if (nums[i] == i) {
                continue;
            }
            
            res  &= nums[i];
        }

        return std::max(0, res);
    }
};