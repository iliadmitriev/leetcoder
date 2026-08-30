#include <vector>
using std::vector;

class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        const auto b = nums.begin();
        const auto m = std::ranges::min_element(nums) - b; // min index
        const auto M = std::ranges::max_element(nums) - b; // max index
        
        const int n = nums.size();
        int l = m, r = M;
        if (l > r) {
            std::swap(l, r);
        }

        /*
                l+1   n-r
          |======>    <=====|
          |======>====>     |
          |      <====<=====|
         */
        return std::min(l + 1 + n - r, std::min(r + 1, n - l));
    }
};