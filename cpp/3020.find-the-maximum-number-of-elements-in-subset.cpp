#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <vector>

using std::vector;

class Solution {
public:
    int maximumLength(vector<int>& nums) {
        /*
        1,1,1,1,2,2,4,4,16,16,256
        */

        int res = 0;

        std::unordered_map<int, int> cnt;
        for (int num : nums) {
            cnt[num]++;
        }

        // count ones at start
        res = std::max(res, cnt[1] & 1 ? cnt[1] : cnt[1] - 1);
        cnt.erase(1); // and drop them

        vector<std::pair<int, int>> cache(cnt.begin(), cnt.end());
        std::ranges::sort(cache);

        std::unordered_map<int, int> prefix;

        for (auto [num, c] : cache) {
            const int prev = std::sqrt(num);

            if ((prev * prev == num) && (cnt[prev] >= 2) &&
                (prefix[prev] > 0)) {
                prefix[num] = 2 + prefix[prev];
            } else {
                prefix[num] = 1;
            }

            res = std::max(res, prefix[num]);
        }

        return res;
    }
};