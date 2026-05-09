class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_map<int, int> cache;
        for (int num: nums) {
            cache[num]++;
        }

        int res = 0;
        for (auto [_, v]: cache) {
            if (v == 1) {
                return -1;
            }

            res += v / 3;
            if (v % 3) {
                res++;
            }
        }

        return res;
    }
};