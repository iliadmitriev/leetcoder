class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> counter;

        for (auto num: arr) {
            counter[num]++;
        }

        unordered_set<int> cache;
        for (auto [_, v]: counter) {
            if (cache.find(v) != cache.end()) {
                return false;
            }

            cache.insert(v);
        }

        return true;
    }
};