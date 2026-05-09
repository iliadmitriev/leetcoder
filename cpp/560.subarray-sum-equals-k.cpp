class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        
        // cache for counting prefixes
        unordered_map<int, int> cache;
        cache[0] = 1; // there is one empty array that sums up to 0

        int sum = 0;
        int res = 0;

        for (int num: nums) {
            sum += num;
            res += cache[sum - k];
            cache[sum]++;
        }

        return res;
    }
};