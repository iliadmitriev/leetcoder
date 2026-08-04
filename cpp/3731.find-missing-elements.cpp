class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        const int start = std::ranges::min(nums);
        const int end = std::ranges::max(nums);

        std::unordered_set<int> cache(nums.begin(), nums.end());
        std::vector<int> res;

        const int alloc = end - start + 1 - cache.size();

        if (alloc > 0) {
            res.reserve(alloc);
        }

        for (int v = start; v <= end; v++) {
            if (cache.find(v) == cache.end()) {
                res.push_back(v);
            }
        }

        return res;
    }
};