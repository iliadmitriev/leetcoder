class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        unordered_map<int, int> cache;
        vector<vector<int>> res;
        int row;

        for (int num: nums) {

            row = cache.find(num) != cache.end() ? cache[num] + 1 : 0;
            cache[num] = row;

            if (row >= res.size()) {
                res.resize(row + 1);
            }

            res[row].push_back(num);
        }

        return res;
    }
};