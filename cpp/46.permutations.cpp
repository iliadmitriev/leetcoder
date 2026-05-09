class Solution {
private:
    vector<vector<int>> res;

    void gen(vector<int>& nums, int curr) {
        if (curr == nums.size()) {
            res.push_back(nums);
            return;
        };

        for (int i = curr; i < nums.size(); i++) {
            std::swap(nums[i], nums[curr]);
            gen(nums, curr + 1);
            std::swap(nums[i], nums[curr]);
        };
    }

public:
    vector<vector<int>> permute(vector<int>& nums) {

        gen(nums, 0);
        return res;
    }
};