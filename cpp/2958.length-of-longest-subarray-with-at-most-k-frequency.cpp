#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        const int n = nums.size();

        if (k >= n) {
            return n;
        }
        
        int j = 0, largest = 0;
        unordered_map<int, int> cnt;

        for (int i = 0; i < n; i++) {
            cnt[nums[i]]++;

            while (j < i && cnt[nums[i]] > k) {
                cnt[nums[j++]]--;
            }

            largest = std::max(largest, i - j + 1);
        }

        return largest;
    }
};