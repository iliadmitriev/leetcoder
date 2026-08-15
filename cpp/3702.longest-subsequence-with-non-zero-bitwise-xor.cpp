class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        const int all = std::ranges::fold_left(nums, 0, std::bit_xor<>());
        const int nonZero =
            std::ranges::count_if(nums, [](int v) { return v; });

        if (all) {
            return nums.size();
        }

        if (nonZero) {
            return nums.size() - 1;
        }

        return 0;
    }
};