class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        auto [min, max] = std::ranges::minmax(nums);
        return 1LL * k * (max - min);
    }
};