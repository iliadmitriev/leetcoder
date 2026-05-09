class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int out = 0;
        unordered_map<int, int> cache;
        for (const auto& num : nums) {
            if (cache.find(num) != cache.end()) {
                out += cache[num];
            }
            cache[num]++;
        }
        return out;
    }
};