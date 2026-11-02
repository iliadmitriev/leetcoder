#include <algorithm>
#include <vector>
#include <numeric>
#include <cmath>

using std::vector;

class Solution {
public:
    int minMoves2(vector<int>& nums) {
        const auto mid_it = nums.begin() + nums.size() / 2;
        std::nth_element(nums.begin(), mid_it, nums.end());
        const int mid = *mid_it;

        return std::accumulate(
            nums.begin(), nums.end(), 0,
            [mid](int acc, int v) -> int { return acc + std::abs(mid - v); });
    }
};