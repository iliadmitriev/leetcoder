class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        for (auto num : nums) {
            counter[num]++;
        }
        vector<int> keys; keys.resize(counter.size());
        std::transform(counter.begin(), counter.end(), keys.begin(), [](const auto& p){
            return p.first;
        });
        std::sort(keys.begin(), keys.end(), [&](const auto& a, const auto& b) {
            return counter[a] > counter[b];
        });

        return vector<int>(keys.begin(), keys.begin() + k);
    }
};