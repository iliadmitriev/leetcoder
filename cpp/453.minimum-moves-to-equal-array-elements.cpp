#include <vector>
#include <algorithm>

class Solution {
public:
    int minMoves(vector<int>& nums) {
        auto min_i = std::ranges::min_element(nums);
        long long total = std::ranges::fold_left(nums, 0LL, std::plus<>{});

        return total - 1LL * nums.size() * *min_i;
    }
};