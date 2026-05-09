class Solution {
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        
        unordered_map<int, int> cache;
        std::function get_cost = [&cache, &nums, &cost](int base) -> long {
            if (cache.find(base) != cache.end()) {
                return cache[base];
            }
            long res = 0;
            int n = nums.size();
            for (int i = 0; i < n; i++) {
                res += (long)cost[i] * abs(base - nums[i]);
            }
            return res;
        };

        int lo = *min_element(nums.begin(), nums.end());
        int hi = *max_element(nums.begin(), nums.end());
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (get_cost(mid) > get_cost(mid + 1)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return get_cost(lo);
    }
};